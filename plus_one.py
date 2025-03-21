from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = str(int(''.join(map(str, digits))) + 1)
        return list(map(int, digits))
