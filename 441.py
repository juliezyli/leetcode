def arrangeCoins(self, n: int) -> int:
        i = 1
        count = 0
        if n == 1:
            return 1
        while n > 0:
            n -= i
            i += 1
            count += 1
        if n == 0:
            return count 
        return count - 1