class Solution:
    def repeatMatrix(self, nums: List[int]) -> Dict:
        res = dict()
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeatMatrix = self.repeatMatrix(nums)
        repeatMatrixSort = dict(sorted(repeatMatrix.items(), key=lambda item: item[1], reverse=True))
        return list(repeatMatrixSort.keys())[:k]