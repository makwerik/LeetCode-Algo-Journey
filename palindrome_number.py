class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            return int(''.join(list(reversed(str(x))))) == x
        except ValueError:
            return False