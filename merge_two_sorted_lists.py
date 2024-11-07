# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Тут пришлось обратиться за помощью, иначе я вообще не понял, что к чему и как это работает.
    В итоге получилось что-то такое: Представим, что ListNode - это вагончик поезда.
    В вагончике хранится число (val) и указатель на следующий вагончик (next).
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Создаю новый пустой вагончик, с него начнём собирать наш поезд"""
        dummy = ListNode()

        """Это текущий вагончик, куда я буду присоединять другие"""
        current = dummy

        """
        Пока у поездов есть вагончики, я буду сравнивать их значения и присоединять по очереди к текущему вагончику
        """
        while list1 and list2:
            """Смотрю, какое число меньше в вагончике list1 or list2"""
            if list1.val < list2.val:
                """Если число меньше, то присоединяю это число к текущему вагончику"""
                current.next = list1
                """Переходим к следующему числу в вагончике list1"""
                list1 = list1.next
            else:
                """Иначе присоединяю вагончик из list2"""
                current.next = list2
                """Переходим к следующему числу в вагончике"""
                list2 = list2.next

            """Теперь текущий вагончик становится следующим"""
            current = current.next

        """Если один из вагончиков закончился, то присоединяю оставшийся вагончик"""
        current.next = list1 if list1 else list2

        """Возвращаю объединенный поезд"""
        return dummy.next