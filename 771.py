def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)
        stones = list(stones)
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count