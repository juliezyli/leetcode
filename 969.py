def pancakeSort(self, arr: List[int]) -> List[int]:
        final = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            final.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return final