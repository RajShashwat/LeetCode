class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x<=9:
            return True
        elif x%10 == 0 and x!= 0:
            return False
        rev = 0
        cpy = x
        while cpy != 0:
            cpy, num = divmod (cpy, 10)
            rev = rev * 10 + num
            if rev == cpy:
                return True
        return True if rev == x else False
