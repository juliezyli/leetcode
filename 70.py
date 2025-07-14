# classic memoization problem
def helpermethod(self, n, memoization):
        if n == 0 or n == 1:
            return 1
        if n not in memoization: 
            memoization[n] = self.helpermethod(n - 1, memoization) + self.helpermethod(n - 2, memoization)
        return memoization[n]

def climbStairs(self, n: int) -> int:
    memoization = {}
    return self.helpermethod(n, memoization)