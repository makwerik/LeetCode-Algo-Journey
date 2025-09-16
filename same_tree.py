# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        Проверка схожести деревьев. Алгоритм работы:
            1. Если оба узла пусты - деревья одинаковы.
            2. Если один из узлов пуст - деревья разные.
            3. Если значения узлов не совпадают - деревья разные.
            4. Иначе рекурсивно проверяем левое и правое поддерево:
               деревья одинаковые тогда и только тогда,
               когда одинаковы их левые поддеревья И одинаковы правые.

            Пример:
            Два дерева:
                p = [1,2,3] и q = [1,2,3]
                - Корни равны (1 == 1) → идём в рекурсию.
                - Слева (2 == 2) → True, справа (3 == 3) → True.
                - True and True → итог True.
        """

        # Если оба узла пусты - деревья одинаковы
        if p is None and q is None:
            return True
        # Если один ищз узлов пустой - деревья разные
        elif p is None or q is None:
            return False
        # Если значения не равны - деревья разные
        elif p.val != q.val:
            return False
        # Иначе проверяем левое поддерево и правое (если хоть 1 вернёт False) - деревья разные
        # p = [1,2,3], q = [1,2,3]
        # Сравниваем корни: оба 1 ✔
        # Вызываем рекурсию:
        # для левых (2 и 2) → вернётся True
        # для правых (3 и 3) → вернётся True
        # True and True → возвращаем True.
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)