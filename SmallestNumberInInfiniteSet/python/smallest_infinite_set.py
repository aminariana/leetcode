from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.next_smallest = 1
        self.heap = []

    def popSmallest(self) -> int:
        if not len(self.heap) or self.heap[0] > self.next_smallest:
            result = self.next_smallest
            self.next_smallest += 1
            return result
        else:
            result = heappop(self.heap)
            # dedup the heap during pop
            while len(self.heap) and self.heap[0] == result:
                heappop(self.heap)
            # dedup across heap and range to behave like a unique set
            if self.next_smallest == result:
                self.next_smallest += 1
            return result
        
    def addBack(self, num: int) -> None:
        return heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)