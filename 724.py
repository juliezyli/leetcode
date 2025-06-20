def pivotIndex(self, nums: List[int]) -> int:
        curr = 0
        total = sum(nums)
        for i in range(len(nums)):
            if curr == total - curr - nums[i]:
                return i
            curr += nums[i]
        return -1