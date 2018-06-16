class Solution(object):
    def flipInvertRow(self, row):
        size = len(row)
        for i in range(size // 2):
            row[i], row[size-i-1] = 1 - row[size-i-1], 1 - row[i]
        if size % 2 != 0:
            row[size//2] = 1 - row[size//2]
        return row
    
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for idx, row in enumerate(A):
            A[idx] = self.flipInvertRow(row)
        return A