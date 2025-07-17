def countBits(self, n: int) -> List[int]:
        final = [] 
        i = 0 
        while i <= n:
            count = 0
            for number in bin(i)[2:]:
                if int(number) == 1:
                    count += 1
            final.append(count)
            i += 1
        return final