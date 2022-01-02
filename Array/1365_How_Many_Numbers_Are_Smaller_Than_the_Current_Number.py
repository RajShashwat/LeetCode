class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c=0
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    c+=1
            output.append(c)
            c=0
        return output
