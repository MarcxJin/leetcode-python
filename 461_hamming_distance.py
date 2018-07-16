class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xornum = x ^ y
        retval = 0
        while xornum > 0:
            retval += xornum % 2
            xornum //= 2
        return retval