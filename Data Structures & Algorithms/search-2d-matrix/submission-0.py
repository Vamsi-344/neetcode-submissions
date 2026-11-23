class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        singleList = []
        for i in matrix:
            singleList.extend(i)
        left = 0
        right = len(singleList) - 1
        while left <= right:
            mid = left + (right - left)//2
            if singleList[mid] == target:
                return True
            elif singleList[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False