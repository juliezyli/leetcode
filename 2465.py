def distinctAverages(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0 
        nums.sort() 
        unique = set()
        left, right = 0, len(nums) - 1 
        while left < right:
            avg = (nums[left] + nums[right]) / 2.0
            unique.add(avg)
            left += 1 
            right -= 1 
        return len(unique)