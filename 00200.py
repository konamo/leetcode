class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for ii in range(n)] for jj in range(m)]
        
        def dfs(y, x):
            if visited[y][x]:
                return
            
            visited[y][x] = True
            
            for next_y, next_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if 0 <= next_y < m and 0 <= next_x < n:
                    if grid[next_y][next_x] == '1':
                        dfs(next_y, next_x)
                            
            return
        
        
        count = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1' and not visited[y][x]:
                    count += 1
                    dfs(y, x)
                
                
        return count
        
