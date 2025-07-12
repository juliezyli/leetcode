def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        final = 0
        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                final = max(final, i - j + 1)
        return final