class Solution:
    def climbStairs(self, n: int) -> int:
        if n > 0:
            if n == 1:
                return 1
            elif n == 2:
                return 2
            a = 1
            b = 2
            for i in range(n-2):
                a, b = b, a+b
                print(a)
                print(b)
            return b
        else:
            return 0
        