class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                
                box_index = (r//3, c//3)
                if r not in rows:
                    rows[r] = set()
                
                if c not in cols:
                    cols[c] = set()

                if box_index not in boxes:
                    boxes[box_index] = set()
                
                if value in rows[r]:
                    return False
                
                if value in cols[c]:
                    return False
                
                if value in boxes[box_index]:
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)
            
        return True
