class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        output = []
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    break
    
        return output
