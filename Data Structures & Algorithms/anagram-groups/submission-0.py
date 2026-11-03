class Solution:
    def getCharSet(self, s: str) -> Tuple:
        res = [0] * 26
        for i in s:
            res[ord(i)-ord("a")] += 1
        return tuple(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[self.getCharSet(s)].append(s)
        return list(res.values())
            
