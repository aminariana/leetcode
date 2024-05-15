from collections.abc import Generator
from functools import cache
from queue import Empty, Queue
from threading import Thread
from requests import get
from bs4 import BeautifulSoup
from collections import deque
from typing import List, Dict


class Crawler:
    def __init__(self):
        self.log = []

    def logger(self, message):
        """Business logic to run on each page's data.
        You should call this at least once per unique page crawled."""
        self.log.append(message)

    @cache
    def get_page_data(self, page_link: str) -> tuple[str, int]:
        """Returns the page data for a given link to a page and its http status code.
        e.g. get_page_data(“www.wikipedia.com”) -> HTML for Wikipedia's web page."""
        response = get(page_link)
        return (response.content, response.status_code)

    def get_links(self, html: str) -> Generator[str]:
        """Returns a list of links parsed from the input HTML"""
        soup = BeautifulSoup(html, features="html.parser")
        for link in soup.findAll("a"):
            href = link.get("href")
            if href and href.startswith("http"):
                yield href

    def process(self, page_link: str, html: str) -> None:
        """Business logic to run on each page's data. You should call this at least once per unique page crawled."""
        print(f"Processed {page_link} (content-length: {len(html)})")

    def crawl(self, page, depth_max: int):
        q = deque([(page, 0)])
        visited = set([page])
        while len(q):
            current_page, current_depth = q.popleft()
            print(f"q size: {len(q)}, depth {current_depth}, page: {current_page}")
            page_data, status_code = self.get_page_data(current_page)
            self.process(current_page, page_data)
            self.logger((current_page, status_code))

            if current_depth < depth_max:
                for link in self.get_links(page_data):
                    if link not in visited:
                        q.append((link, current_depth + 1))
                        visited.add(link)
        return self.log


class MultiThreadedCrawler(Crawler):
    def __init__(self):
        super().__init__()

    def crawl(self, page, depth_max: int, visit_max: int = 0, thread_count: int = 1, timeout=5):
        q = Queue()
        visited = set()

        def work(thread_id):
            print(f"Thread entered: {thread_id}")
            try:
                while True:
                    current_page, current_depth = q.get(timeout=timeout)
                    visited.add(current_page)

                    print(
                        f"thread_id: #{thread_id}, backlog: {q.qsize()}, visited: {len(visited)}, depth {current_depth}\npage: {current_page}"
                    )
                    page_data, status_code = self.get_page_data(current_page)
                    self.process(current_page, page_data)
                    self.logger((current_page, status_code))

                    if current_depth < depth_max and (not visit_max or len(visited) <= visit_max):
                        for link in self.get_links(page_data):
                            if link not in visited:
                                visited.add(link)
                                q.put((link, current_depth + 1))
                                print(f"\t#{thread_id} push: {link}")
                    q.task_done()
            except Empty:
                print(f"Thread exited on idle: {thread_id}")

        q.put((page, 0))
        thread_pool = []
        for thread_id in range(thread_count):
            thread = Thread(target=work, args=(thread_id,))
            thread.start()
            thread_pool.append(thread)
        print("Thread pool awaiting ...")
        q.join()
        for thread in thread_pool:
            thread.join()
        print("Thread pool finished.")
        return self.log


class MockCrawler(MultiThreadedCrawler):
    def __init__(self, data: Dict[str, List[str]]):
        super().__init__()
        self.page_to_html = {}
        self.html_to_links = {}
        i = 0
        for key, value in data.items():
            page_data = str(i)
            self.page_to_html[key] = page_data
            self.html_to_links[page_data] = value.copy()
            i += 1
        print("Page to HTML:")
        print(self.page_to_html)
        print("HTML to links:")
        print(self.html_to_links)

    def get_page_data(self, page: str) -> tuple[str, int]:
        status_code = 200
        if page not in self.page_to_html:
            status_code = 404
        return (self.page_to_html.get(page, ""), status_code)

    def get_links(self, html: str) -> List[str]:
        return self.html_to_links.get(html, [])

    def process(self, page: str, html: str):
        pass


def main():
    # crawler = Crawler()
    # crawler.crawl("https://www.wikipedia.com", 2)
    crawler = MultiThreadedCrawler()
    crawler.crawl(
        "https://www.wikipedia.com", depth_max=2, visit_max=20, thread_count=10
    )
    print(crawler.log)


if __name__ == "__main__":
    main()
