class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        row_max = [max(row) for row in grid]
        col_max = [max([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret += (min(row_max[i], col_max[j]) - grid[i][j])
        return ret