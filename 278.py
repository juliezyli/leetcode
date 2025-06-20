def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n 
        while left < right:
            middle = int((left + right) / 2)
            if (not isBadVersion(middle - 1) and isBadVersion(middle)):
                return middle
            if not isBadVersion(middle):
                left = middle + 1
            else: 
                right = middle 
        return left