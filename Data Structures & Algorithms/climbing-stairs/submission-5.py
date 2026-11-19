class Solution:
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

    def climbStairs(self, n: int) -> int:
        ways = 0
        for i in range(n//2 + 1):
            j = n - 2 * i
            onePath = []
            onePath.extend([2]*i)
            onePath.extend([1]*j)
            combinations = self.factorial(i+j)
            deDupDeduction = self.factorial(i) * self.factorial(j)
            possibleWaysCount = int(combinations/deDupDeduction)
            ways += possibleWaysCount
        return ways