def minOperations(self, nums: List[int], k: int) -> int:
        sum = 0
        for number in nums:
            sum += number
        if sum % k == 0:
            return 0 
        return abs(sum - ((sum // k) * k))