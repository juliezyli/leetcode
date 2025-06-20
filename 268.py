def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        if nums[0] != 0:
            return 0
        while i < len(nums) - 1:
            if (nums[i] + 1) != nums[i+1]:
                return nums[i] + 1
            i += 1
        return len(nums)