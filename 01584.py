class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm, MST
        if not points:
            return 0
        
        nums = len(points)
        visited = [False] * nums
        dist = [float('inf')] * nums
        dist[0] = 0
        hp = [(0, 0)]
        heapify(hp)
        
        while hp:
            _, index = heappop(hp)
            
            if visited[index]:
                continue
                
            visited[index] = True
            x, y = points[index]
            for jj, next_p in enumerate(points):
                if not visited[jj]:
                    next_x, next_y = next_p
                    d = abs(x - next_x) + abs(y - next_y)
                    if d < dist[jj]:
                        dist[jj] = d
                        heappush(hp, (d, jj))
        
        return sum(dist)
        
        
                    
        
