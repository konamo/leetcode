class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        nn = len(board) ** 2
        arr = [0]
        visited = set([1])
        pos = 1

        for ii, row in enumerate(board[::-1]):
            if ii % 2:
                arr += row[::-1]
            else:
                arr += row

        search_queue = [1]
        steps = 0

        while search_queue:
            next_search_queue = []
            for pos in search_queue:
                if pos >= nn:
                    return steps

                for next in range(pos + 1, pos + 7):
                    if next <= nn:
                        if arr[next] == -1:
                            if next not in visited:
                                next_search_queue.append(next)
                                visited.add(next)
                        else:
                            if arr[next] not in visited:
                                next_search_queue.append(arr[next])
                                visited.add(arr[next])
            search_queue = next_search_queue
            steps += 1

        return -1





def main():
    s = Solution()
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    print("1: " + str(s.snakesAndLadders(board)))

    board = [[-1, -1], [-1, 3]]
    print("2: " + str(s.snakesAndLadders(board)))

    board = [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]
    print("3: " + str(s.snakesAndLadders(board)))

    return


if __name__ == '__main__':
    main()