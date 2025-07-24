def isHappy(self, n: int) -> bool:
    finished = set()
    while n != 1:
        if n in finished: 
            return False 
        finished.add(n)
        n = sum(pow(int(digit), 2) for digit in str(n))
    return True