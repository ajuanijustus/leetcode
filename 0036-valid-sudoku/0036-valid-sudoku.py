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
                    if x in row[i]:
                        return False
                    else:
                        row[i].append(x)
                else:
                    row[i] = [x]
                    
                if j in col.keys():
                    if x in col[j]:
                        return False
                    else:
                        col[j].append(x)
                else:
                    col[j] = [x]
                
                box_id = str(i//3) + "_" + str(j//3)
                if box_id in box.keys():
                    if x in box[box_id]:
                        return False
                    else:
                        box[box_id].append(x)
                else:
                    box[box_id] = [x]

        return True