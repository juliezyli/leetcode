def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[:n]
        second = nums[n:]
        ans = []
        for i in range(len(first)):
            ans.append(first[i])
            ans.append(second[i])
        return ans