def hammingDistance(self, x: int, y: int) -> int:
    # binary of a number can be found through the bin() method 
    # the ^ is bitwise exclusive OR
    return bin(x ^ y).count('1') 