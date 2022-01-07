class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums)
        while i > 1:
            i -= 1
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)
