class MedianFinder:

    def __init__(self):
        self.hl = []
        self.hr = []
        self.nl = self.nr = 0
        
    def addNum(self, num: int) -> None:
        # l = -self.lheap[0] if self.lheap else float("-inf")
        # r = self.rheap[0] if self.rheap else float("inf")
        # # print("push", l, r , num)
        # if len(self.lheap) == len(self.rheap):
        #     if num < l:
        #         heapq.heappush(self.lheap, -num)
        #         num = -heapq.heappop(self.lheap)
        #     heapq.heappush(self.rheap, num)
        # else:
        #     if num > r:
        #         heapq.heappush(self.rheap, num)
        #         num = heapq.heappop(self.rheap)
        #     heapq.heappush(self.lheap, -num)


        l = -self.hl[0] if self.hl else float("-inf")
        r = self.hr[0] if self.hr else float("inf")

        if self.nl==self.nr:
            self.nr += 1
            if num < l:
                heapq.heappush(self.hl, -num)
                heapq.heappop(self.hl)
                heapq.heappush(self.hr, l)
            else:
                heapq.heappush(self.hr, num)
        else:
            self.nl += 1
            if num > r:
                heapq.heappush(self.hr, num)
                heapq.heappop(self.hr)
                heapq.heappush(self.hl, -r)
            else:
                heapq.heappush(self.hl, -num)

        # print(self.hl, self.hr)

    def findMedian(self) -> float:
        if self.nl == self.nr:
            return (-self.hl[0]+self.hr[0])/2.0
        else:
            return self.hr[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()