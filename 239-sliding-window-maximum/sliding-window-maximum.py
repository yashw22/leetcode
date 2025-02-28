class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []
        q = deque()
        
        l, r = 0, k

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])

        for r in range(k, len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            l+=1
            if l>q[0]:
                q.popleft()
            
            res.append(nums[q[0]])

        return res



        