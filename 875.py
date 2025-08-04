def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        final = right 
        while left <= right:
            middle = (left + right) // 2 
            time = sum((p + middle - 1) // middle for p in piles)
            if time <= h:
                final = middle 
                right = middle - 1 
            else:
                left = middle + 1 
        return final