class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if not grid:
            return -1

        if grid[0][0] != 0:
            return -1

        n = len(grid)
        if grid[n - 1][n - 1] != 0:
            return -1

        steps = 1
        search_queue = [[0, 0]]
        visited = [[False] * n for ii in range(n)]

        while search_queue:
            next_search_queue = []
            for y, x in search_queue:
                if y == n - 1 and x == n - 1:
                    return steps

                visited[y][x] = True

                for y1 in [y+1, y, y-1]:
                    for x1 in [x+1, x, x-1]:
                        if 0 <= y1 < n and 0 <= x1 < n:
                            if not visited[y1][x1]:
                                if grid[y1][x1] == 0:
                                    next_search_queue.append([y1, x1])
                                    visited[y1][x1] = True
            steps += 1
            search_queue = next_search_queue

        return -1





def main():
    s = Solution()
    grid = [[0,1],[1,0]]
    print("1: " + str(s.shortestPathBinaryMatrix(grid)))

    grid = [[0,0,0],[1,1,0],[1,1,0]]
    print("2: " + str(s.shortestPathBinaryMatrix(grid)))

    grid = [[1,0,0],[1,1,0],[1,1,0]]
    print("3: " + str(s.shortestPathBinaryMatrix(grid)))

    return



if __name__ == '__main__':
    main()
