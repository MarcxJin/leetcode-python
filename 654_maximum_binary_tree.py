class Solution:
    def searchMax(self, nums):
        maxi, maxidx = nums[0], 0
        for idx, num in enumerate(nums):
            if maxi < num:
                maxi, maxidx = num, idx
        return maxidx
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            tree_node = TreeNode(nums[0])
            return tree_node
        ctr_idx = self.searchMax(nums)
        tree_node = TreeNode(nums[ctr_idx])
        tree_node.left = self.constructMaximumBinaryTree(nums[:ctr_idx])
        tree_node.right =  self.constructMaximumBinaryTree(nums[ctr_idx+1:])
        return tree_node