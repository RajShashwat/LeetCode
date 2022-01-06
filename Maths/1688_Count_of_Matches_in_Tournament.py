class Solution:
    def numberOfMatches(self, n: int) -> int:
        s = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                s = s + n
            else:
                n = n  // 2
                s = s + n
                n = n + 1
            
        return s
