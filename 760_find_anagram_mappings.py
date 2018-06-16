class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {}
        for idx, elem in enumerate(B):
            d[elem] = idx
        return [d[elem] for elem in A]