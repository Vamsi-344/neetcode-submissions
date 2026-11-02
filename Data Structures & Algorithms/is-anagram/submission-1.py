class Solution:
    def charRepSet(self, s: str) -> dict:
        res = dict()
        for i in s:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        if self.charRepSet(s) == self.charRepSet(t):
            return True
        else:
            return False