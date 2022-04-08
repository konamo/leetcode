from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            curr = curr.child[c]
        curr.isWord = True


class Solution:
    def wordBreak2(self, s: str, wordDict: list[str]) -> bool:
 	    d = [False] * len(s)    
 	    for i in range(len(s)):
 		    for w in wordDict:
 			    if w == s[i-len(w)+1:i+1] and (i-len(w) == -1 or d[i-len(w)]):
 				    d[i] = True
 	    return d[-1]

    def wordBreak3(self, s: str, wordDict: list[str]) -> bool:
        search_list = [s]
        visited = set()

        while search_list:
            string = search_list.pop(0) # pop(0) = BFS, pop() = DFS

            for word in wordDict:
                #if string.find(word) == 0:
                if string.startswith(word):
                    new_string = string[len(word):]
                    if new_string == '':
                        return True

                    if new_string not in visited:
                        search_list.append(new_string)
                        visited.add(new_string)

        return False

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        root = TrieNode()
        for word in wordDict:
            root.addWord(word)

        def dp(start):
            if start == n:  # Found a valid way to break words
                return True

            curr = root
            for end in range(start + 1, n + 1):  # O(N)
                c = s[end-1]
                if c not in curr.child:
                    break
                curr = curr.child[c]
                if curr.isWord and dp(end):
                    return True
            return False

        return dp(0)

def main():
    s = Solution()
    s1 = "leetcode"
    wordDict = ["leet","code"]
    print(s.wordBreak(s1, wordDict))

    s1 = "applepenapple"
    wordDict = ["apple","pen"]
    print(s.wordBreak(s1, wordDict))

    s1 = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(s.wordBreak(s1, wordDict))

    s1 = "aaaaaaa"
    wordDict = ["aaaa","aaa"]
    print(s.wordBreak(s1, wordDict))
    
    return



if __name__ == '__main__':
    main()
