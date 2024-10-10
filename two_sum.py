from typing import List


class Solution:
    def check_index(self, result, nums):
        index_ = []
        for r in result:
            if len(index_) == len(result):
                break
            for i, k in enumerate(nums):
                if r == k:
                    index_.append(i)
        return index_

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for n in nums[i + 1:]:
                if nums[i] + n == target:
                    return self.check_index([nums[i], n], nums)

