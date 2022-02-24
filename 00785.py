class Solution:
    def isBipartite2(self, graph: list[list[int]]) -> bool:
        RED  = 1
        BLUE = 2

        g = {}
        for ii, jj in enumerate(graph):
            for kk in jj:
                if ii in g:
                    g[ii].append(kk)
                else:
                    g[ii] = [kk]

        is_possible = True
        curr_color = RED
        next_color = BLUE
        color = [0] * len(graph)

        def dfs(node):
            nonlocal is_possible
            nonlocal curr_color
            nonlocal next_color

            color[node] = curr_color

            if node in g:
                for next_node in g[node]:
                    if color[next_node] != 0:
                        if color[next_node] != next_color:
                            is_possible = False
                    else:
                        curr_color, next_color = next_color, curr_color
                        dfs(next_node)
                        curr_color, next_color = next_color, curr_color

        for ii in range(len(graph)):
            if color[ii] == 0:
                dfs(ii)

        return is_possible


    # The idea is that each node has to be in a different set than its neighbors, and all its neighbors should be in the same set.
    def isBipartite(self, graph: list[list[int]]) -> bool:
        def find(x: int) -> int:
            while root[x] != x:
                x = root[x]
            return x

        def union(x: int, y: int):
            rootx = find(x)
            rooty = find(y)
            root[rootx] = rooty

        root = [ii for ii in range(len(graph))]

        for node, neighbors in enumerate(graph):
            for ii in neighbors:
                if find(ii) == find(node):
                    return False
            for jj, kk in zip(neighbors, neighbors[1:]):
                union(jj, kk)

        return True


def main():
    s = Solution()
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print("1: " + str(s.isBipartite(graph)))

    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print("2: " + str(s.isBipartite(graph)))

    graph = [[4],[],[4],[4],[0,2,3]]
    print("3: " + str(s.isBipartite(graph)))

    graph = [[3], [2, 4], [1], [0, 4], [1, 3]]
    print("4: " + str(s.isBipartite(graph)))

    return



if __name__ == '__main__':
    main()
