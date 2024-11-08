from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                j += 1
                # Тут по индексу j в списке, я записываю новое уникально значение
                nums[j] = nums[i]

        return j + 1