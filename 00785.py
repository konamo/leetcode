class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        RED  = 1
        BLUE = 2

        g = {}
        for ii in range(len(graph)):
            for jj in graph[ii]:
                if ii in g:
                    g[ii].append(jj)
                else:
                    g[ii] = [jj]

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






def main():
    s = Solution()
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print("1: " + str(s.isBipartite(graph)))

    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print("2: " + str(s.isBipartite(graph)))

    graph = [[4],[],[4],[4],[0,2,3]]
    print("3: " + str(s.isBipartite(graph)))

    return



if __name__ == '__main__':
    main()
