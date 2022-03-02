from collections import deque


class Solution:
    def combine2(self, n: int, k: int) -> list[list[int]]:
        """
        dfs
        """

        ans = []

        def dfs(start: int, path: list):
            if len(path) == k:
                ans.append(path)
                return
            for ii in range(start, n + 1):
                dfs(ii + 1, path + [ii])

        dfs(1, [])
        return ans



    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        bfs
        :param n:
        :param k:
        :return:
        """
        queue = deque([([], 0)])

        return self.bfs(queue, k, n)

    def bfs(self, queue, k, n):
        result = []

        while queue:
            curPath, idx = queue.popleft()

            if len(curPath) == k:
                result.append(curPath)
                continue

            for i in range(idx+1, n+1):
                queue.append((curPath + [i], i))

        return result



def main():
    s = Solution()
    print("1: " + str(s.combine(5, 2)))

    print("2: " + str(s.combine2(20, 16)))

    return



if __name__ == '__main__':
    main()