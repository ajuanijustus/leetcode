class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        while(t <= b):
            y = t + ((b-t) // 2)
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                t = y + 1
            elif y == 0 or matrix[y-1][x] < target:
                li = matrix[y]
                l, r = 0, len(li) - 1
                while (l <= r):
                    i = l + (r-l) // 2
                    if li[i] > target:
                        r = i - 1
                    elif li[i] < target:
                        l = i + 1
                    else:
                        return True
                return False
            else:
                b = y - 1
        return False