class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return [0, 1]
        
        for i in range(len(nums)):
            for j in range(len(nums[i+1:])):
                if nums[i]+nums[i+1+j]==target:
                    return [i, i+1+j]

            
                