class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = -1
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                idx = i-1
                break

        if idx==-1:
            nums.sort()
            return

        low = n-1
        while idx<low:
            if nums[idx]<nums[low]:
                break
            low -= 1

        nums[idx], nums[low] = nums[low], nums[idx]
        nums[idx+1:] = sorted(nums[idx+1:])