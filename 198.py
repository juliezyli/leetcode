def rob(self, nums: List[int]) -> int:
        dont, do = 0, 0
        for num in nums:
            dont, do = do, max(do, dont + num)
        return do