class NumMatrix:
    # brute force (solution 1)
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0

        for x in range(col1, col2 + 1):
            for y in range(row1, row2 + 1):
                s += self.matrix[y][x]

        return s
        
    # caching the rows
    def __init__(self, matrix):
        self.s = []
        for ii in range(len(matrix)):
            # add 0 to the first to avoid the corner case
            t = [0]
            dp = 0
            for jj in range(len(matrix[0])):
                dp += matrix[ii][jj]
                t.append(dp)
            self.s.append(t[:])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for ii in range(row1, row2 + 1):
            s += self.s[ii][col2 + 1] - self.s[ii][col1]
        return s

    # smart caching
    def __init__(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        # add 0 to the first to avoid the corner case
        self.s = [[0 for ii in range(col+1)] for ii in range(row+1)]

        for ii in range(1, row+1):
            for jj in range(1, col+1):
                self.s[ii][jj] = self.s[ii-1][jj] + self.s[ii][jj-1] - self.s[ii-1][jj-1] + matrix[ii-1][jj-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.s[row2+1][col2+1] - self.s[row2+1][col1] - self.s[row1][col2+1] + self.s[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
