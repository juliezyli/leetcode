def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        number = n * n
        total_weight = number * w
        while total_weight > maxWeight: 
            number -= 1
            total_weight = (number) * w
        return number