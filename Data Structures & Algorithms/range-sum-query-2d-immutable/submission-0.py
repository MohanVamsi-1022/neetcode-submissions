class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,columns = len(matrix),len(matrix[0])
        self.sum_matrix = [[0] * (columns+1) for _ in range(rows+1)]
        for r in range(rows):
            prefix_sum = 0
            for c in range(columns):
                prefix_sum += matrix[r][c]
                above = self.sum_matrix[r][c+1]
                self.sum_matrix[r+1][c+1] = prefix_sum + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2 = row1 + 1,col1 + 1,row2 + 1,col2 + 1
        bottom_right = self.sum_matrix[r2][c2]
        above = self.sum_matrix[r1-1][c2]
        left = self.sum_matrix[r2][c1-1]
        top_left = self.sum_matrix[r1-1][c1-1]
        return bottom_right - above - left + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)