class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = dict()
        for i, v in enumerate(nums):
            if target - v in visited_nums:
                return [visited_nums[target-v], i]
            else:
                visited_nums[v] = i
                continue