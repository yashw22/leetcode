class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)

        # heap = [(-v,k) for k,v in count.items()]
        # heapq.heapify(heap)

        # res = []
        # for _ in range(k):
        #     _, item = heapq.heappop(heap)
        #     res.append(item)

        # return res
        
        # ------optimal-------
        counts = Counter(nums)

        heap = []
        for item, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, [count, item])
            elif heap[0][0] < count:
                heapq.heappop(heap)
                heapq.heappush(heap, [count,item])
        
        return [item for _, item in heap]