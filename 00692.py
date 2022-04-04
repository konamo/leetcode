from collections import Counter
import heapq
from functools import total_ordering

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
    
class Solution(object):
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
