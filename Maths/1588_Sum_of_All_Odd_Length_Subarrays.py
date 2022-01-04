class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l, ans = len(arr), 0
        for x in range(l):
            sub_sum = 0
            for i in range(x, l):
                sub_sum += arr[i]
                if not (i - x) % 2:
                    ans += sub_sum
        return ans
