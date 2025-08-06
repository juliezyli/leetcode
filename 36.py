def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 
        columns = [0] * 9
        boxes = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue 
                num = ord(board[i][j]) - ord('1')
                mask = 1 << num 
                box_index = (i // 3) * 3 + (j // 3)
                if (rows[i] & mask) or (columns[j] & mask) or (boxes[box_index] & mask):
                    return False 
                rows[i] |= mask
                columns[j] |= mask 
                boxes[box_index] |= mask
        return True