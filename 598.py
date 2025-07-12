def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        ops.sort()
        right = []
        for operation in ops:
            right.append(operation[1])
        right.sort()
        return ops[0][0] * right[0]