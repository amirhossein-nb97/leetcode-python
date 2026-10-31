class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        miss = 0
        duplicated = 0
        nums.sort()

        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == nums[i - 1]:
                duplicated = nums[i]
            if i not in nums:
                miss = i

        return [duplicated, miss]
