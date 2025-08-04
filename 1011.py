def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right: 
            middle = (left + right) / 2
            need = 1 
            curr = 0 
            for weight in weights:
                if curr + weight > middle:
                    need += 1 
                    curr = 0 
                curr += weight 
            if need > days:
                left = middle + 1 
            else:
                right = middle 
        return int(left)