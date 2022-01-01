class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a =nums[0]
        x = [a]
        for i in range(1,len(nums)):
            a = a+nums[i]
            x.append(a)
        return x
        
