def longestArithSeqLength(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return length
        longest = 2 
        dp = [{} for _ in range(length)]
        for i in range(length):
            for j in range(i):
                difference = nums[i] - nums[j]
                dp[i][difference] = dp[j].get(difference, 1) + 1
                longest = max(longest, dp[i][difference])
        return longest