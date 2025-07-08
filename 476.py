def findComplement(self, num: int) -> int:
        binary = list(bin(num))[2:]
        new_list = []
        for number in binary:
            if int(number) == 1:
                new_list.append(0)
            else: 
                new_list.append(1)
        return int(''.join(str(num) for num in new_list), 2)