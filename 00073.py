class Solution:
    def setZeroes2(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        z = set()

        for ii in range(m):
            for jj in range(n):
                if matrix[ii][jj] == 0:
                    for aa in range(m):
                        z.add((aa, jj))
                    for bb in range(n):
                        z.add((ii, bb))

        for x, y in z:
            matrix[x][y] = 0

        return

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        is_col = False

        for ii in range(m):
            if matrix[ii][0] == 0:
                is_col = True

            for jj in range(1, n):
                if matrix[ii][jj] == 0:
                    matrix[0][jj] = 0
                    matrix[ii][0] = 0

        for jj in range(1, n):
            if matrix[0][jj] == 0:
                for ii in range(m):
                    matrix[ii][jj] = 0

        for ii in range(m):
            if matrix[ii][0] == 0:
                for jj in range(n):
                    matrix[ii][jj] = 0
        if is_col:
            for ii in range(m):
                matrix[ii][0] = 0

        return


def main():
    s = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] 
    s.setZeroes(matrix)

    return



if __name__ == '__main__':
    main()
