class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        low = 0
        high = len(s) - 1
        numOfTimesToReplace = (n//2 if n%2 == 0 else n//2+1)
        while numOfTimesToReplace != 0:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
            numOfTimesToReplace -= 1
        