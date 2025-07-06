def isPowerOfTwo(self, n: int) -> bool:
    # & is used to compare the bits of integers 
    return (n > 0) and ((n & (n-1)) == 0)