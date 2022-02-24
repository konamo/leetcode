class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minute = -1
        fresh = 0
        total = 0
        search_queue = []

        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == 2:
                    search_queue.append([y, x])
                    total += 1
                elif grid[y][x] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        total += fresh

        while search_queue:
            size = len(search_queue)
            total -= size

            for ii in range(size):
                y, x = search_queue.pop(0)

                grid[y][x] = 2

                for y1, x1 in [[y, x - 1], [y, x + 1], [y - 1, x], [y + 1, x]]:
                    if 0 <= y1 < len(grid) and 0 <= x1 < len(grid[0]):
                        if [y1, x1] not in search_queue and grid[y1][x1] == 1:
                            search_queue.append([y1, x1])
            minute += 1

        if total == 0:
            return minute
        else:
            return -1






def main():
    s = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print("1: " + str(s.orangesRotting(grid)))

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print("2: " + str(s.orangesRotting(grid)))

    grid = [[0,2]]
    print("3: " + str(s.orangesRotting(grid)))

    grid = [[0,1]]
    print("4: " + str(s.orangesRotting(grid)))

    grid = [[0]]
    print("5: " + str(s.orangesRotting(grid)))

    return



if __name__ == '__main__':
    main()
