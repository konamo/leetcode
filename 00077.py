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



    def combine3(self, n: int, k: int) -> list[list[int]]:
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




    def combine4(self, n: int, k: int) -> list[list[int]]:
        # DP
        # at time n, there are 2 options
        # option1, no change from prev: res[n-1][k]
        # option2, add number n to prev: res[n-1][k-1]
        # take care of the first part when its element is []
        ans = []
        if n >= k > 0:
            for f in self.combine4(n - 1, k):
                if f:
                    ans += [f]

            for f in self.combine4(n - 1, k - 1):
                ans += [f + [n]]
        else:
            return [[]]

        return ans

        #return [f for f in self.combine(n-1, k) if f] + [f + [n] for f in self.combine(n-1, k-1)] if n >= k > 0 else [[]]



def main():
    s = Solution()
    print("1: " + str(s.combine3(5, 2)))

    print("2: " + str(s.combine2(20, 16)))

    return



if __name__ == '__main__':
    main()