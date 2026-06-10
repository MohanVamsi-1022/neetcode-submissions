class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        res = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        if not (top <= bottom):
            return False
        row = mid
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False        

        


        