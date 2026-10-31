class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1=nums[0:n]
        nums2=nums[n:2*n]
        res=[] 
        for i in range(n):
            res.append(nums1[i])
            res.append(nums2[i])
        
        return res
