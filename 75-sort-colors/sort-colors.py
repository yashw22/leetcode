class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j, k = 0, 0, n-1

        while j<=k:
            if nums[j]==1:
                j += 1
            elif nums[j]==2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            elif nums[j]==0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1


        