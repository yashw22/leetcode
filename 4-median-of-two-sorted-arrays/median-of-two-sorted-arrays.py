class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = total//2

        if n1>n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        l, r = 0, n1-1
        while True:
            i = l + (r-l)//2
            j = half-i-2

            al = nums1[i] if i>-1 else float("-inf")
            bl = nums2[j] if j>-1 else float("-inf")
            ar = nums1[i+1] if i+1<n1 else float("inf")
            br = nums2[j+1] if j+1<n2 else float("inf")

            if al<=br and bl<=ar:
                if total%2:
                    return min(ar, br)
                else:
                    return (max(al,bl)+min(ar,br))/2.0

            if al>br:
                r = i-1
            else:
                l = i+1
