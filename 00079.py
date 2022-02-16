class Solution:
    def __init__(self):
        self.word = None
        self.board = None
        self.visited = None

    def out_of_bound(self, x: int, y: int) -> bool:
        if x < 0 or x >= len(self.board):
            return True
        elif y < 0 or y >= len(self.board[0]):
            return True
        else:
            return False

    def is_visited(self, x: int, y: int) -> bool:
        return self.visited[x][y]

    def add_visited(self, x: int, y: int):
        self.visited[x][y] = 1

    def remove_visited(self, x: int, y: int):
        self.visited[x][y] = 0

    def reset_visited(self):
        self.visited = []
        for ii in range(len(self.board)):
            self.visited.append([0] * len(self.board[0]))
        return


    def exist(self, board: list[list[str]], word: str) -> bool:
        self.word = word
        self.board = board

        if len(self.board) == 0:
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                self.reset_visited()
                if self.search(x, y, 0):
                    return True
        return False
    
    def search(self, x: int, y: int, d: int) -> bool:
        if self.out_of_bound(x, y):
            return False
        elif self.is_visited(x, y):
            return False
        elif self.word[d] != self.board[x][y]:
            return False
        elif d == len(self.word) - 1:
            return True
        c = self.board[x][y]
        self.board[x][y] = 0
        #self.add_visited(x, y)
        found = self.search(x - 1, y, d + 1) or \
                self.search(x + 1, y, d + 1) or \
                self.search(x, y - 1, d + 1) or \
                self.search(x, y + 1, d + 1)
        #self.remove_visited(x, y)
        self.board[x][y] = c
        return found


def main():
    s = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(s.exist(board, "ABCCED"))

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    print(s.exist(board, "ABCB"))

    board = [["a", "b"], ["c", "d"]]
    print(s.exist(board, "cdba"))

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    print(s.exist(board, "ABCESEEEFS"))

    board = [["A", "Z", "A", "A"], ["B", "B", "B", "B"], ["B", "C", "B", "B"], ["B", "B", "B", "B"], ["B", "B", "B", "B"]]
    print(s.exist(board, "BBBBBBBBBBBCBZ"))

    return


if __name__ == "__main__":
    main()
