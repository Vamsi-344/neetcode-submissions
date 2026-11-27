class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            listS = list(s)
            listS.pop(i)
            newStr = ''.join(listS)
            if newStr == newStr[::-1]:
                return True
        return False