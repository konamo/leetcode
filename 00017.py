class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []


        letter = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'],
                ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        visited = [False] * 26
        ret = []
        length = len(digits)
        ans = []
        def dfs(digits):
            if len(ret) == length:
                ans.append(''.join(ret))
                return

            for index, d in enumerate(digits):
                for l in letter[int(d)]:
                    ret.append(l)
                    dfs(digits[index+1:])
                    ret.pop()



        dfs(digits)
        return ans



def main():
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))

    digits = ""
    print(s.letterCombinations(digits))

    digits = "2"
    print(s.letterCombinations(digits))

    digits = "22"
    print(s.letterCombinations(digits))
    return



if __name__ == '__main__':
    main()
