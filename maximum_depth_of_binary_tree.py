# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # Если корень пуст - глубина дерева = 0
        if root is None:
            return 0

        # Иначе рекурсивно вызываем метод и считаем глубину левого поддерева, затем правого.
        # Глубину рекурсии считаем так: сначала доходит до листьев (None → 0),
        # потом при возврате назад на каждом уровне добавляется +1.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))




