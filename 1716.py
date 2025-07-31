def totalMoney(self, n: int) -> int:
        final = 0 
        first = 1 
        while n > 0:
            for day in range(min(n, 7)):
                final += first + day 
            n -= 7 
            first += 1 
        return final