def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                ans.append(nums[i])
        return ans