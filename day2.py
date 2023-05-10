class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = int(str(x)[::-1])
        if x == reversed_x:
            return True

