from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ret = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            ret[key] += [s]

        return list(ret.values())


    def get_permutation(self, some_string, idx=0):
        if idx == len(some_string) - 1:       
            print("".join(some_string))
        for j in range(idx, len(some_string)):
            words_list = [c for c in some_string]   
            words_list[idx], words_list[j] = words_list[j], words_list[idx]
       
            self.get_permutation(words_list, idx + 1)

    def get_permutation2(self, some_string):
        n = len(some_string)
        visited = [False] * n

        l = []
        def dfs():
            if len(l) == n:
                print(l)
                return
            for ii in range(n):
                if not visited[ii]:
                    visited[ii] = True
                    l.append(some_string[ii])
                    dfs()
                    visited[ii] = False
                    l.pop()
        dfs()

    def get_permutation3(self, some_string):
        n = len(some_string)
        r = []
        def dfs(r, strs):
            if len(r) == n:
                print(r)
                return
            for ii, s in enumerate(strs):
                r.append(s)
                dfs(r, strs[:ii] + strs[ii+1:])
                r.pop()
        dfs([], some_string)

def main():
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(strs))

    strs = ["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]
    print(s.groupAnagrams(strs))

    print(s.get_permutation3("abc"))
    return



if __name__ == '__main__':
    main()
