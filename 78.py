# classic backtracking problem 
def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(idx, curr):
            if idx == len(nums):
                result.append(curr[:])
                return
            backtrack(idx + 1, curr)
            curr.append(nums[idx])
            backtrack(idx + 1, curr)
            curr.pop()
        backtrack(0, [])
        return result