class Solution:
    def __init__(self):
        self.heights = None
        
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ret = []
        self.heights = heights
        
        for x in range(len(heights[0])):
            for y in range(len(heights)):
                if self.findPathtoPacific(100000, x, y) and self.findPathtoAtlantic(100000, x, y):
                    ret.append([y, x])
                    
        return ret
    
    
    def findPathtoPacific(self, height, x, y):
        if x < 0 or y < 0:
            return True
        elif x >= len(self.heights[0]) or y >= len(self.heights):
            return False
        elif height >= self.heights[y][x]:
            h = self.heights[y][x]
            self.heights[y][x] = 100000
            found = self.findPathtoPacific(h, x - 1, y) or \
                    self.findPathtoPacific(h, x + 1, y) or \
                    self.findPathtoPacific(h, x, y - 1) or \
                    self.findPathtoPacific(h, x, y + 1)
            self.heights[y][x] = h
            return found
        else:
            return False
        
    def findPathtoAtlantic(self, height, x, y):
        if x >= len(self.heights[0]) or y >= len(self.heights):
            return True
        elif x < 0 or y < 0:
            return False
        elif height >= self.heights[y][x]:
            h = self.heights[y][x]
            self.heights[y][x] = 100000
            found = self.findPathtoAtlantic(h, x - 1, y) or \
                    self.findPathtoAtlantic(h, x + 1, y) or \
                    self.findPathtoAtlantic(h, x, y - 1) or \
                    self.findPathtoAtlantic(h, x, y + 1)
            self.heights[y][x] = h
            return found
        else:
            return False


    def pacificAtlantic2(self, heights: list[list[int]]) -> list[list[int]]:
        ret = []
        self.heights = heights
        p = [[False] * len(self.heights[0]) for ii in range(len(self.heights))]
        a = [[False] * len(self.heights[0]) for ii in range(len(self.heights))]
        
        for x in range(len(self.heights[0])):
            self.dfs(x, 0, 0, p)
            self.dfs(x, len(self.heights) - 1, 0, a)

        for y in range(len(self.heights)):
            self.dfs(0, y, 0, p)
            self.dfs(len(self.heights[0]) - 1, y, 0, a)

        for x in range(len(self.heights[0])):
            for y in range(len(self.heights)):
                if p[y][x] and a[y][x]:
                    ret.append([y, x])
                    
        return ret

    def dfs(self, x: int, y: int, height: int, o: list[list[int]]):
        if x < 0 or y < 0 or x >= len(self.heights[0]) or y >= len(self.heights):
            return
        elif o[y][x]:
            return
        elif height <= self.heights[y][x]:
            o[y][x] = True
            h = self.heights[y][x]
            self.heights[y][x] = -1
            self.dfs(x + 1, y, h, o)
            self.dfs(x - 1, y, h, o)
            self.dfs(x, y - 1, h, o)
            self.dfs(x, y + 1, h, o)
            self.heights[y][x] = h

    def pacificAtlantic3(self, heights: list[list[int]]) -> list[list[int]]:
        ret = []
        self.heights = heights
        p = [[False] * len(self.heights[0]) for ii in range(len(self.heights))]
        a = [[False] * len(self.heights[0]) for ii in range(len(self.heights))]
        
        for x in range(len(self.heights[0])):
            self.bfs(x, 0, p)
            self.bfs(x, len(self.heights) - 1, a)

        for y in range(len(self.heights)):
            self.bfs(0, y, p)
            self.bfs(len(self.heights[0]) - 1, y, a)

        for x in range(len(self.heights[0])):
            for y in range(len(self.heights)):
                if p[y][x] and a[y][x]:
                    ret.append([y, x])
                    
        return ret

    def bfs(self, x: int, y: int, o: list[list[int]]):
        search_node = []
        search_node.append([y, x])

        while search_node:
            y, x = search_node.pop(0)
            o[y][x] = True

            if y >= 1 and o[y-1][x] == False and self.heights[y-1][x] >= self.heights[y][x]:
                if [y-1, x] not in search_node:
                    search_node.append([y-1, x])
            if y + 1 < len(self.heights) and o[y+1][x] == False and self.heights[y+1][x] >= self.heights[y][x]:
                if [y+1, x] not in search_node:
                    search_node.append([y+1, x])
            if x >= 1 and o[y][x-1] == False and self.heights[y][x-1] >= self.heights[y][x]:
                if [y, x-1] not in search_node:
                    search_node.append([y, x-1])
            if x + 1 < len(self.heights[0]) and o[y][x+1] == False and self.heights[y][x+1] >= self.heights[y][x]:
                if [y, x+1] not in search_node:
                    search_node.append([y, x+1])

        return




def main():
    s = Solution()

    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(s.pacificAtlantic3(heights))

    heights = [[1,2,3,4,5,6,7,8,9,10,11,12],[44,45,46,47,48,49,50,51,52,53,54,13],[43,80,81,82,83,84,85,86,87,88,55,14],[42,79,108,109,110,111,112,113,114,89,56,15],[41,78,107,128,129,130,131,132,115,90,57,16],[40,77,106,127,140,141,142,133,116,91,58,17],[39,76,105,126,139,144,143,134,117,92,59,18],[38,75,104,125,138,137,136,135,118,93,60,19],[37,74,103,124,123,122,121,120,119,94,61,20],[36,73,102,101,100,99,98,97,96,95,62,21],[35,72,71,70,69,68,67,66,65,64,63,22],[34,33,32,31,30,29,28,27,26,25,24,23]]
    print(s.pacificAtlantic3(heights))


if __name__ == '__main__':
    main()
