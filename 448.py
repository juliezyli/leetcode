def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = []
        for i in range(1, len(nums) + 1):
            numbers.append(i)
        return list(set(numbers) - set(nums))