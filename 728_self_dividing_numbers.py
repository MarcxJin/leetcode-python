class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isDividingNumber(num):
            for n in str(num):
                if n == '0' or num % int(n) != 0:
                    return False
            return True
        
        retval = []
        for num in range(left, right+1):
            if isDividingNumber(num):
                retval.append(num)
        return retval