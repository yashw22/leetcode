class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix.reverse()
        # n = len(matrix)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        n = len(matrix)
        for i in range(floor(n/2)):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



        