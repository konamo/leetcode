class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0 for _ in range(n+1)] for _ in range(m+1)]
        path[0][1] = 1
        for y in range(m):
            for x in range(n):
                path[y+1][x+1] = path[y+1][x] + path[y][x+1]

        return path[m][n]



def main():
    s = Solution()
    m = 3
    n = 7
    print(s.uniquePaths(m, n))


    m = 3
    n = 2
    print(s.uniquePaths(m, n))





    return



if __name__ == '__main__':
    main()
