class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = str(n)
        p = 1
        s = 0
        for i in x:
            p = p * int(i)
            s = s + int(i)
        return p-s
