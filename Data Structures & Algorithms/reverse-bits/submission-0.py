class Solution:
    def reverseBits(self, n: int) -> int:
        givenIntBits = bin(n)[2:].zfill(32)
        rev = givenIntBits[::-1]
        return int(rev,2)