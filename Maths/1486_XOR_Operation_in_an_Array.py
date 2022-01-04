class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l = []
        for i in range(n):
            l.append(start + 2 * i)
        r = reduce(lambda x, y: x ^ y, l)
        return r
