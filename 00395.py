class Solution:
    def longestSubstring2(self, s: str, k: int) -> int:
        longest = 0

        for ii in range(len(s)):
            for jj in range(ii+1, len(s)+1):
                if self.is_qualify(s[ii:jj], k):
                    longest = max(longest, jj - ii)

        return longest

    def is_qualify(self, s, k):
        for ii in s:
            if s.count(ii) < k:
                return False
        return True

    def longestSubstring3(self, s: str, k: int) -> int:
        # divide and conquer
        return self.longestSubstringUtil(s, k);

    def longestSubstringUtil(self, s, k):
        if len(s) < k:
            return 0

        for mid in range(len(s)):
            if s.count(s[mid]) >= k:
                continue
            # mid is the first invalid one
            midNext = mid + 1

            # skip the mid invalid ones
            while midNext < len(s) and s.count(s[midNext]) < k: 
                midNext += 1

            return max(self.longestSubstringUtil(s[:mid], k),
                    self.longestSubstringUtil(s[midNext:], k))
        # we're here just because no invalid was found, so just return the whole string
        return len(s)

    def longestSubstring(self, s: str, k: int) -> int:
        # this idea is hard to understand
        maxUnique = self.getMaxUniqueLetters(s)
        result = 0

        for currUnique in range(1, maxUnique + 1):
            windowStart = 0
            windowEnd = 0
            idx = 0
            unique = 0
            countAtLeastK = 0


            d = {}
            while windowEnd < len(s):
                if unique <= currUnique:
                    if d.get(s[windowEnd], 0) == 0:
                        unique += 1
                    d[s[windowEnd]] = d.get(s[windowEnd], 0) + 1
                    if d[s[windowEnd]] == k:
                        countAtLeastK += 1
                    windowEnd += 1
                else:
                    if d.get(s[windowStart], 0) == k:
                        countAtLeastK -= 1
                    d[s[windowStart]] = d.get(s[windowStart], 0) - 1
                    if d[s[windowStart]] == 0:
                        unique -= 1
                    windowStart += 1

                if unique == currUnique and unique == countAtLeastK:
                    result = max(windowEnd - windowStart, result);
        return result

    def getMaxUniqueLetters(self, s):
        #return len(set(list(s)))
        d = {}
        for ii in s:
            d[ii] = d.get(ii, 0) + 1
        return len(d)


def main():
    s = Solution()
    s1 = "aaabb"
    k = 3
    print(s.longestSubstring(s1, k))

    s1 = "ababbc"
    k = 2
    print(s.longestSubstring(s1, k))

    s1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    k = 1
    print(s.longestSubstring(s1, k))
    return




if __name__ == '__main__':
    main()
        # end is the last '0' of the string
