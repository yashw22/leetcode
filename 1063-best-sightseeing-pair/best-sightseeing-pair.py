class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        maxLeft = values[0]
        maxScore = 0

        for i in range(1,n):
            curr = values[i]-i
            maxScore = max(maxScore, maxLeft + curr)
            maxLeft = max(maxLeft, values[i]+i)

        return maxScore