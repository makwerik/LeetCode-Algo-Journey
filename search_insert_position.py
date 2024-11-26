from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Проверка на то, что таргет меньше первого элемента
        if target < nums[0]:
            return 0

        # Проверка на то, что таргет больше последнего элемента
        if target > nums[-1]:
            return len(nums)

        # Проверка где таргет должен быть вставлен
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            elif nums[i] < target < nums[i + 1]:
                return i + 1

        # Проверка, если таргет совпадает с последним элементом
        if nums[-1] == target:
            return len(nums) - 1

        return len(nums)