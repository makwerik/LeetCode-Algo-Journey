from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Получаем голову, примерно список такой [1, 1, 2]
        current = head

        # Цикл по списку
        while current and current.next:
            # Если дубликат найден
            # current.val [1 (индекс 0)] == current.next.val [1 (индекс 1)]
            if current.val == current.next.val:
                # Меняем ссылку путём перепрыгивания через дубликат
                # current.next [1 (индекс 1)] = current.next.next [2 (индекс 2)]
                current.next = current.next.next
            # Иначе переходим дальше по значениям
            else:
                current = current.next

        return head
