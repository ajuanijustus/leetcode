class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = {}
        box = {}
        row = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                x = board[i][j]
                if x == ".":
                    continue
                else:
                    x = int(x)
                    
                if i in row.keys():
                    row[i].append(x)
                else:
                    row[i] = [x]
                    
                if j in col.keys():
                    col[j].append(x)
                else:
                    col[j] = [x]
                
                box_id = str(i//3) + "_" + str(j//3)
                if box_id in box.keys():
                    box[box_id].append(x)
                else:
                    box[box_id] = [x]
        
        for r in row.values():
            if len(r) != len(set(r)):
                return False
        for c in col.values():
            if len(c) != len(set(c)):
                return False
        for b in box.values():
            if len(b) != len(set(b)):
                return False
        return True