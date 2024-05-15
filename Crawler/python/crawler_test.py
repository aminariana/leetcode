from Crawler.python.crawler import MockCrawler


class TestCrawler:
    def test_invalid_page(self):
        crawler = MockCrawler(
            {
                "page1": [],
            }
        )
        assert [("page2", 404)] == crawler.crawl("page2", 3)

    def test_no_cycles_no_duplicates(self):
        crawler = MockCrawler(
            {
                "page1": ["page2", "page3"],
                "page2": ["page4", "page5"],
                "page5": ["page6"],
                "page6": ["page7"],
            }
        )
        assert [
            ("page1", 200),
            ("page2", 200),
            ("page3", 404),
            ("page4", 404),
            ("page5", 200),
            ("page6", 200),
        ] == crawler.crawl("page1", 3)

    def test_duplicates_no_cycles(self):
        crawler = MockCrawler(
            {
                "page1": ["page2", "page3"],
                "page2": ["page3", "page4", "page5"],
                "page5": ["page6", "page3"],
                "page6": ["page7"],
            }
        )
        assert [
            ("page1", 200),
            ("page2", 200),
            ("page3", 404),
            ("page4", 404),
            ("page5", 200),
            ("page6", 200),
        ] == crawler.crawl("page1", 3)

    def test_cycles(self):
        crawler = MockCrawler(
            {
                "page1": ["page1", "page2", "page3"],
                "page2": ["page3", "page4", "page5", "page1"],
                "page5": ["page6", "page3", "page2"],
                "page6": ["page7", "page3", "page1"],
            }
        )
        assert [
            ("page1", 200),
            ("page2", 200),
            ("page3", 404),
            ("page4", 404),
            ("page5", 200),
            ("page6", 200),
            ('page7', 404),
        ] == crawler.crawl("page1", 5)
