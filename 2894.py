def differenceOfSums(self, n: int, m: int) -> int:
        lst1 = []
        lst2 = []
        for i in range(1, n + 1):
            if i % m == 0:
                lst2.append(i)
            else:
                lst1.append(i)
        return sum(lst1) - sum(lst2)