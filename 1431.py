def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= most:
                result.append(True)
            else:
                result.append(False)
        return result