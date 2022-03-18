class Solution:
    def spiralOrder2(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        ret = []


        def spiralOne(x, y, n, m):
            for ii in range(x, n):
                ret.append(matrix[y][ii])
            for ii in range(y + 1, m - 1):
                ret.append(matrix[ii][n - 1])
            if y + 1 < m:
                for ii in range(n - 1, x - 1, -1):
                    ret.append(matrix[m - 1][ii])
            if x + 1 < n:
                for ii in range(m - 2, y, -1):
                    ret.append(matrix[ii][x])

        ii = 0
        jj = 0
        while ii < (n + 1) // 2 and jj < (m + 1) // 2:
            spiralOne(ii, jj, n - ii, m - jj)
            ii += 1
            jj += 1


        return ret




    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        ret = []
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # Traverse Right
            for ii in range(colBegin, colEnd + 1):
                ret.append(matrix[rowBegin][ii])
            rowBegin += 1
            
            # Traverse Down
            for ii in range(rowBegin, rowEnd + 1):
                ret.append(matrix[ii][colEnd])
            colEnd -= 1

            if rowBegin <= rowEnd:
                # Traverse Left
                for ii in range(colEnd, colBegin - 1, -1):
                    ret.append(matrix[rowEnd][ii])
            rowEnd -= 1
            
            if colBegin <= colEnd:
                # Traver Up
                for ii in range(rowEnd, rowBegin - 1, -1):
                    ret.append(matrix[ii][colBegin])
            colBegin += 1

        return ret








def main():
    s = Solution()

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    l = s.spiralOrder(matrix)
    print(l)

    matrix = [[7],[9],[6]]
    l = s.spiralOrder(matrix)
    print(l)
    return



if __name__ == '__main__':
    main()
