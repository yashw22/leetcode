class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = [[-count, ch] for ch, count in counts.items()]
        heapq.heapify(maxHeap)

        print(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            count, ch = heapq.heappop(maxHeap)
            res += ch
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if count != 0:
                prev = [count, ch]

        return res