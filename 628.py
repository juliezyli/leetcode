def maximumProduct(self, nums: List[int]) -> int:
        negative = []
        positive = []
        nums.sort()
        for number in nums:
            if number <= 0:
                negative.append(number)
            else:
                positive.append(number)
        if len(negative) >= 2 and 0 < len(positive) < 3:
            return negative[0] * negative[1] * positive[len(positive) - 1]
        if len(negative) >= 2 and len(positive) >= 3:
            return max(negative[0] * negative[1] * positive[len(positive) - 1], positive[len(positive) - 1] * positive[len(positive) - 2] * positive[len(positive) - 3])
        return nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3]