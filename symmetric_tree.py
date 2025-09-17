# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        Проверка зеркальности деревьев.
        Алгоритм работы:
            Если корень пуст - значит деревья одинаковы.

            Если корень не пуст, мы проваливаемся в заранее написанную рекурсивную функцию (она так задумана).
            И запускаем череду проверок:
                Если левое поддерево и правое пустое - деревья зеркальны.
                Если одно из поддеревьев не пустое - деревья разные.
                Если значения в левом и правом дереве разные - деревья разные.
                Иначе рекурсивно проходимся по дереву снова и сначала выполняется левая часть кода, если она возвращает
                    истину(True) выполняем вторую часть кода по такой же схеме.
                    1) Первая часть кода *сравнение внешних узлов*:
                                symmetric(left.left, right.right)

                                 and (логическое "И")
                    2) Вторая часть кода *сравнение внутренних узлов*
                                  symmetric(left.left, right.right)
        """

        if root is None:
            return True

        def symmetric(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False

            return symmetric(left.left, right.right) and symmetric(left.right, right.left)

        return symmetric(left=root.left, right=root.right)