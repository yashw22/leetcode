class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i])
            if nums[idx] < 0:
                return idx
            else:
                nums[idx] *= -1