class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
    
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        
        res.append(nums[q[0]])

        l = 0
        for r in range(k, len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            l += 1
            if l>q[0]:
                q.popleft()

            res.append(nums[q[0]])

        return res