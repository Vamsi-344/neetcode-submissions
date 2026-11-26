class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.hashMap.append([key, value])
        else:
            for i in self.hashMap:
                if i[0] == key:
                    i[1] = value

    def get(self, key: int) -> int:
        for i in self.hashMap:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) != -1:
            for i in range(len(self.hashMap)):
                if self.hashMap[i][0] == key:
                    self.hashMap.remove([self.hashMap[i][0], self.hashMap[i][1]])
                    break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)