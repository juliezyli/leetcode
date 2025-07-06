def addDigits(self, num: int) -> int:
        numbers = list(str(num))
        while len(numbers) != 1:
            nums = 0
            for number in numbers:
                nums += int(number)
            numbers = list(str(nums))
        return int(''.join([str(num) for num in numbers]))