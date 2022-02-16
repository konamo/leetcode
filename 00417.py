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



def main():
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    s = Solution()
    print(s.pacificAtlantic(heights))

if __name__ == '__main__':
    main()
