def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        horizontal = []
        for row in mat:
            horizontal.extend(row)
        final = []
        if r * c != len(horizontal):
            return mat
        for row_i in range(r):
            final.append(horizontal[row_i * c : row_i * c + c])
        return final