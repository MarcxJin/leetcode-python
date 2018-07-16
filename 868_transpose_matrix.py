class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(A), len(A[0])
        retval = [[None for _ in range(row)] for __ in range(col)]
        for r in range(row):
            for c in range(col):
                retval[c][r] = A[r][c]
        return retval