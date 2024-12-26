class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = [(-v,k) for k,v in count.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            _, item = heapq.heappop(heap)
            res.append(item)

        return res
        
