class Solution:
    WHITE = 1 # node which is not processed
    GRAY  = 2 # node which is in DFS
    BLACK = 3 # node which has been added to schedule

    # dfs
    def findOrder2(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if numCourses <= 1:
            return [0]

        d: dict = {}
        for dst, src in prerequisites:
            if src in d:
                d[src].append(dst)
            else:
                d[src] = [dst]

        color: list[int] = [self.WHITE] * numCourses
        sch: list[int] = []
        is_possible: bool = True

        def dfs(node: int):
            nonlocal is_possible

            if not is_possible:
                return

            color[node] = self.GRAY

            if node in d:
                for next_node in d[node]:
                    if color[next_node] == self.WHITE:
                        dfs(next_node)
                    elif color[next_node] == self.GRAY:
                        is_possible = False

            color[node] = self.BLACK
            sch.append(node)

        for node in range(numCourses):
            if color[node] == self.WHITE:
                dfs(node)

        sch.reverse()
        if is_possible:
            return sch
        else:
            return []

    # Kahn
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if numCourses <= 1:
            return [0]

        d: dict = {}
        indegree = [0] * numCourses
        for dest, src in prerequisites:
            if src in d:
                d[src].append(dest)
            else:
                d[src] = [dest]

            # Record each node's in-degree
            indegree[dest] += 1

        zero_indegree_queue = [k for k in range(numCourses) if indegree[k] == 0]
        sch = []

        while zero_indegree_queue:
            node = zero_indegree_queue.pop(0)

            # Reduce in-degree for all the neighbors
            if node in d:
                for next_node in d[node]:
                    indegree[next_node] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[next_node] == 0:
                        zero_indegree_queue.append(next_node)

            sch.append(node)

        if len(sch) == numCourses:
            return sch
        else:
            return []



def main():
    s = Solution()

    numCourses = 2
    prereq = [[1, 0]]
    print("1 " + str(s.findOrder(numCourses, prereq)))

    numCourses = 2
    prereq = [[0, 1]]
    print("2 " + str(s.findOrder(numCourses, prereq)))

    numCourses = 3
    prereq = [[0, 1], [0, 2], [1, 2]]
    print("3 " + str(s.findOrder(numCourses, prereq)))

    numCourses = 4
    prereq = [[1,0],[2,0],[3,1],[3,2]]
    print("4 " + str(s.findOrder(numCourses, prereq)))

    numCourses = 2
    prereq = [[0,1],[1,0]]
    print("5 " + str(s.findOrder(numCourses, prereq)))

    numCourses = 3
    prereq = [[0,1],[0,2],[1,2]]
    print("6 " + str(s.findOrder(numCourses, prereq)))

    numCourses = 3
    prereq = [[1,0],[1,2],[0,1]]
    print("7 " + str(s.findOrder(numCourses, prereq)))

    numCourses = 4
    prereq = [[2,0],[1,0],[3,1],[3,2],[1,3]]
    print("8 " + str(s.findOrder(numCourses, prereq)))

if __name__ == '__main__':
    main()