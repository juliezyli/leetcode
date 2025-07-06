def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            arr.append(sum)
        return max(arr)