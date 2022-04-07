class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # start position of the sliding window
        start = 0

        # most freq char till now (from index 0)
        # or you could think about it in this way:
        # the most freq char in the longest substring so far
        maxCount = 0

        # longest substring so far
        maxLength = 0

        # freq for the current sliding window
        count = {}

        # set the initial window to be as far as possible
        # and then looks for any substring longer than that
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            maxCount = max(maxCount, count[s[end]])
            
            # the idea is:
            # the length of the substring should be <= most freq char + k
            if end - start + 1 > k + maxCount:
                count[s[start]] -= 1
                start += 1
                update maxCount
            else:
                # update the longest substring if it meets the requirement
                maxLength = max(maxLength, end - start + 1)
        return maxLength


def main():
    s = Solution()
    s1 = "ABAB"
    k = 2
    print(s.characterReplacement(s1, k))

    s1 = "AABABBA"
    k = 1
    print(s.characterReplacement(s1, k))

    s1 = "ABBB"
    k = 2
    print(s.characterReplacement(s1, k))

    s1 = "BAAAB"
    k = 2
    print(s.characterReplacement(s1, k))

    return




if __name__ == '__main__':
    main()
