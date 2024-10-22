class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dictionary = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for symbol in s:
            if symbol in brackets_dictionary.values():
                stack.append(symbol)
                continue
            if len(stack) != 0:
                if brackets_dictionary[symbol] == stack.pop():
                    continue
                else:
                    return False
            return False
        if len(stack) == 0:
            return True
        else:
            return False