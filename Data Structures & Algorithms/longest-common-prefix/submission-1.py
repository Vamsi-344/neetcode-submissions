class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = 0
        while longest <= min([len(i) for i in strs]):
            prefix = strs[0][:longest]
            res = [prefix in i for i in strs]
            if all(res) == True:
                longest += 1
            else:
                break
        if longest == 0:
            return ""
        else:
            return strs[0][:longest-1]