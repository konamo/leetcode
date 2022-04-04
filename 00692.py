from collections import Counter
import heapq

class Solution2:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        ret = sorted(d, key=lambda x: (-d[x], x))
        
        return ret[:k]

class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            # we're sorting from low freq to high freq
            # and the reverse of lexicographical order
            # because we will do the reverse again later
            return self.word > other.word
        return self.count < other.count
    
class Solution3(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Counter(words)   
        
        freqs = []
        for word, count in counts.items():
            if len(freqs) == k:
                if Element(count, word) > freqs[0][0]:
                    heapq.heappushpop(freqs, (Element(count, word), word))
            else:
                heapq.heappush(freqs, (Element(count, word), word))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]




class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.word = None
        
class Solution4(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        buckets = [TrieNode() for _ in range(len(words) + 1)]
        for word in count:
            root = buckets[count[word]]
            self.add(word, root)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i].children:
                continue
            self.getWord(res, buckets[i], k)
            if len(res) >= k:
                return res
        return res
    
    def add(self, word, root):
        for c in word:
            if root.children[ord(c) - ord("a")] == None:
                root.children[ord(c) - ord("a")] = TrieNode()
            root = root.children[ord(c) - ord("a")]
        root.word = word
        
        
    def getWord(self, res, root, k):
        if not root:
            return 
        if len(res) >= k:
            return 
        if root.word:
            res.append(root.word)
        
        for i in range(26):
            self.getWord(res, root.children[i], k)
        return 

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1

        ret = [None] * (len(words) + 1)
        for ii in d:
            if ret[d[ii]] == None:
                ret[d[ii]] = [ii]
            else:
                ret[d[ii]].append(ii)

        ii = len(words)
        res = []
        while ii > 0:
            if ret[ii] == None:
                ii -= 1
            else:
                ret[ii].sort()
                res += ret[ii]
                if len(res) >= k:
                    break
                ii -= 1
        return res[:k]


def main():
    s = Solution()
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    print(s.topKFrequent(words, k))

    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    k = 4
    print(s.topKFrequent(words, k))

    words = ["i","love","leetcode","i","love","coding"]
    k = 3
    print(s.topKFrequent(words, k))
    
    return



if __name__ == '__main__':
    main()
