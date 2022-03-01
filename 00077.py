class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        ans = []

        def dfs(start: int, path: list):
            if len(path) == k:
                ans.append(path)
                return
            for ii in range(start, n + 1):
                dfs(ii + 1, path + [ii])

        dfs(1, [])
        return ans


    def combine2(self, n, k):
        ret = []
        self.dfs(list(range(1, n + 1)), k, [], ret)
        return ret

    def dfs(self, nums, k, path, ret):
        if len(path) == k:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], k, path + [nums[i]], ret)







def main():
    s = Solution()
    print("1: " + str(s.combine(5, 2)))

    return



if __name__ == '__main__':
    main()
