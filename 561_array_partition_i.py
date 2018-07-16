class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum, n = 0, len(nums)
        for i in range(0, n, 2):
            sum += nums[i]
        return sum