class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[float("inf") for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        dp[0][1] = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                dp[y+1][x+1] = min(dp[y+1][x], dp[y][x+1]) + grid[y][x]
        
        return dp[-1][-1]



def main():
    s = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(s.minPathSum(grid))

    grid = [[1,2,3],[4,5,6]]
    print(s.minPathSum(grid))



    return



if __name__ == '__main__':
    main()
