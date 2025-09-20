# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        if not nums: return None
        # Ищем середину
        mid = len(nums) // 2

        # Создаём дерево с корнем посередине
        node = TreeNode(nums[mid])

        # Строим левое поддерево
        node.left = self.sortedArrayToBST(nums[:lenght])
        # Строим правое поддерево, чтобы пропустить середину
        node.right = self.sortedArrayToBST(nums[lenght+1:])

        return node