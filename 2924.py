def findChampion(self, n: int, edges: List[List[int]]) -> int:
        lst = [0] * n
        for winner, loser in edges:
            lst[loser] += 1 
        champion = -1 
        for i in range(n):
            if lst[i] == 0:
                if champion != -1:
                    return -1
                champion = i 
        return champion