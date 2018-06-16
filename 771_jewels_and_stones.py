class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ret = 0
        j_set = set(J)
        for char in S:
            if char in j_set:
                ret += 1
        return ret