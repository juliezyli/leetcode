def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def validMove(r, c, k):
            if r >= n or r < 0 or c >= n or c < 0:
                return 0
            if k == 0:
                return 1 
            return 1/8 * validMove(r + 2, c + 1, k - 1) + 1/8 * validMove(r + 2, c - 1, k - 1) + 1/8 * validMove(r - 2, c + 1, k - 1) + 1/8 * validMove(r - 2, c - 1, k - 1) + 1/8 * validMove(r + 1, c + 2, k - 1) + 1/8 * validMove(r + 1, c - 2, k - 1) + 1/8 * validMove(r - 1, c + 2, k - 1) + 1/8 * validMove(r - 1, c - 2, k - 1)
        return validMove(row, column, k)