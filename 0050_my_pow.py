class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

# Alternative solution

class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        if n % 2: return x * self.myPow(x, n - 1)
        else: return self.myPow(x * x, n // 2)

# Alternative solution

class Solution2:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)
