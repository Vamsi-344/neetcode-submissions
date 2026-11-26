class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        countOfElement = nums.count(val)
        k = len(nums) - countOfElement
        lastIndex = -1
        while countOfElement > 0:
            firstIndex = nums.index(val)
            nums[lastIndex], nums[firstIndex] = nums[firstIndex], nums[lastIndex]
            lastIndex -= 1
            countOfElement -= 1
        return k