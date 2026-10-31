class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max = 0
        s = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                s= s + 1 
            else:
                if s >= max:
                    max = s
                    s = 0
                else:
                    s = 0
            

        if nums[-1] ==1 and s>=max:
            max = s
        return max
