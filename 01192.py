class Solution:
    def criticalConnections2(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        edgeMap = {}
        for a,b in connections:
            if a in edgeMap:
                edgeMap[a].append(b)
            else:
                edgeMap[a] = [b]
            if b in edgeMap:
                edgeMap[b].append(a)
            else:
                edgeMap[b] = [a]

        disc, low, time, ans = [0] * n, [0] * n, [1], []
        def dfs(curr: int, prev: int):
            disc[curr] = low[curr] = time[0]
            time[0] += 1
            for next in edgeMap[curr]:
                if not disc[next]:
                    dfs(next, curr)
                    low[curr] = min(low[curr], low[next])
                elif next != prev:
                    low[curr] = min(low[curr], disc[next])

            if prev != -1 and low[prev] < low[curr]:
                ans.append([prev, curr])

        dfs(0, -1)
        return ans

    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        edgeMap = {}
        for a,b in connections:
            if a in edgeMap:
                edgeMap[a].append(b)
            else:
                edgeMap[a] = [b]
            if b in edgeMap:
                edgeMap[b].append(a)
            else:
                edgeMap[b] = [a]
        res = []
        jump = [-1] * n

        def dfs(v, par, lvl):
            jump[v] = lvl + 1
            for child in edgeMap[v]:
                if child == par:
                    continue
                elif jump[child] == -1:
                    jump[v] = min(jump[v], dfs(child, v, lvl + 1))
                else:
                    jump[v] = min(jump[v], jump[child])

            if jump[v] == lvl + 1 and v != 0:
                res.append([par, v])

            return jump[v]

        dfs(0, -1, 0)
        return res


def main():
    s = Solution()
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    print("1: " + str(s.criticalConnections2(n, connections)))

    n = 5
    connections = [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]
    print("2: " + str(s.criticalConnections2(n, connections)))

if __name__ == "__main__":
    main()