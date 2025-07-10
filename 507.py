import math
def checkPerfectNumber(self, num: int) -> bool:
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i: 
                divisors.append(num // i)
    if sum(divisors) == 2 * num:
        return True
    return False