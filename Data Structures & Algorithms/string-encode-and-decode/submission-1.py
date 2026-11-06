class Solution:
    def encode(self, strs: List[str]) -> str:
        resString = ""
        delimiter = "#"
        for i in strs:
            resString += str(len(i))+delimiter+i
        return resString

    def decode(self, s: str) -> List[str]:
        resList = []
        index = 0
        while index < len(s):
            if s[index+1] == "#":
                len_of_str = int(s[index])
                index += 2
            else:
                j = index
                while s[j] != "#":
                    j+=1
                len_of_str = int(s[index:j])
                index += len(str(len_of_str))+1
            resList.append(s[index:index+len_of_str])
            index += len_of_str
        return resList
