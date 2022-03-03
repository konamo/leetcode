class Solution:
    def generateParenthesis2(self, n: int) -> list[str]:

        ret = []
        first = 0
        second = 0
        def dfs(s):
            nonlocal first, second

            if len(s) == n * 2:
                if s.count('(') == s.count(')') == n:
                    ret.append(s)
            else:
                if first < n:
                    first += 1
                    dfs(s + '(')
                    first -= 1
                if first > second:
                    second += 1
                    dfs(s + ')')
                    second -= 1

        dfs("")

        return ret


    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

def main():
    s = Solution()
    n = 3
    print("1: " + str(s.generateParenthesis(n)))

    n = 1
    print("1: " + str(s.generateParenthesis(n)))


    return




if __name__ == '__main__':
    main()
