class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans_size = 2 * n
        ans = [None] * ans_size
        for i in range (0,  n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans
