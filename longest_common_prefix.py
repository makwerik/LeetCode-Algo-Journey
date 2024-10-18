from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenght_list = len(strs) - 1
        count = 0
        result = []
        for index, symbol in enumerate(strs[0]):
            for s in strs[1:]:
                try:
                    if s[index] == symbol:
                        count += 1
                except IndexError:
                    continue
            if count == lenght_list:
                result.append(symbol)
                count = 0
            else:
                return ''.join(result)
        return ''.join(result)