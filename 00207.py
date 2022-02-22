class Solution:
    # Kahn
    def canFinish2(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if numCourses <= 1:
            return True

        adj_list = {}
        indegree = [0] * numCourses
        for dst, src in prerequisites:
            if src in adj_list:
                adj_list[src].append(dst)
            else:
                adj_list[src] = [dst]

            indegree[dest] += 1

        zero_indegree_queue = [k for k in range(numCourses) if indegree[k] == 0]
        schedule = []
        while zero_indegree_queue:
            node = zero_indegree_queue.pop(0)

            if node in adj_list:
                for next_node in adj_list[node]:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        zero_indegree_queue.append(next_node)

            schedule.append(node)

        if len(schedule) == numCourses:
            return True
        else:
            return False

    # dfs
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        WHITE = 1
        GRAY  = 2
        BLACK = 3

        if numCourses <= 1:
            return True

        adj_list = {}
        for dst, src in prerequisites:
            if src in adj_list:
                adj_list[src].append(dst)
            else:
                adj_list[src] = [dst]

        color = [WHITE] * numCourses
        is_possible = True

        def dfs(node):
            nonlocal is_possible

            if is_possible == False:
                return

            color[node] = GRAY

            if node in adj_list:
                for next_node in adj_list[node]:
                    if color[next_node] == WHITE:
                        dfs(next_node)
                    elif color[next_node] == GRAY:
                        is_possible = False

            color[node] = BLACK
            return

        for node in range(numCourses):
            if color[node] == WHITE:
                dfs(node)

        return is_possible




def main():
    s = Solution()
    numCourses = 2
    prereq = [[1, 0]]
    print("1: " + str(s.canFinish(numCourses, prereq)))






if __name__ == "__main__":
    main()
