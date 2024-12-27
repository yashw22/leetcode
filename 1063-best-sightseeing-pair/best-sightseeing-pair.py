class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        maxLeft = [values[0]] + [0]*(n-1)
        maxScore = 0

        for i in range(1,n):
            curr = values[i]-i
            maxScore = max(maxScore, maxLeft[i-1] + curr)
            maxLeft[i] = max(maxLeft[i-1], values[i]+i)

        return maxScore