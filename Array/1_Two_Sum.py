class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,n in enumerate(nums):
            val = target-n
            if val in hashMap:
                return [hashMap[val], i]
            else:
                hashMap[n] = i         
        return []
