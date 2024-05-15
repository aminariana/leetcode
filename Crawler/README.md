# Crawler

![Hard](https://img.shields.io/badge/Difficulty-Hard-red)


Implement a **Web Crawler** that starts with a given `page` url, scrapes its content, performs a `process` hook function on the content, then visits all the web pages accessible from the hyperlinks. The Crawler continues processing pages until it has hit every page at least `k` deep, where the depth of the original page is `0`.

Return *the URL of all the seen pages in the processing order*.

For convenience, the interface you need may look like this:
```
class Crawler:
    def __init__(self):
        pass

    def get_page_data(self, page_link: str) -> tuple[str, int]:
        """Returns the page data for a given link to a page and its http status code.
        e.g. get_page_data(“www.wikipedia.com”) -> HTML for Wikipedia's web page."""
        pass

    def get_links(self, html: str) -> Generator[str]:
        """Returns a list of links parsed from the input HTML"""
        pass

    def process(self, page_link: str, html: str) -> None:
        """Hook to run on each page's data. You should call this at least once per unique page crawled."""
        pass

    def crawl(self, page, depth_max: int):
        pass
```

**Part 1:**

1. Can you get the correct pages?
2. Can you test that you got the correct pages?
3. Can you avoid revisiting pages in cycles?
4. Can you visit the pages in the breadth order for relevance?

**Part 2:**

If you start with Wikipedia's main page and only go 2 levels deep, you will encounter thousands of pages which take a long time to process. How can the way you process them become much faster? (Code it) -- What's the difference in the orders of complexities of part 1 vs 2?

**Part 3**

Can you mock the Crawler from Part 1 in your tests in a way that it can prove your Part 2 solution?

**Hints**

Part 1: Graph BFS
Part 2: Multi-threading
Part 3: Use mock inheritance

**Comments**

Someone with a heavy Amazon / Java background asked this question with too much pre-occupation with the ability to jump into threading and understanding pre-existing inheritance. Questions like this should be evaluated based on how you approach various sub-problems, not how quickly you can assume a pre-existing contract and solve for its requirements under time crunch. Those interviewers tend to be poor at gathering signal. Nevertheless, this question is a great exercise for gaining some confidence in your ability to multi-thread. Most of the gotchas on part 2 are in understanding thread-safety of Python's Queue, its `get` behavior, and the ability of threads to signal to each other whether some future work is still pending arrival despite the queue being temporarily empty.

I did part 1 in 20 minutes and part 2 in >5 hours, YMMV.