class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for ii in s:
            d[ii] = d.get(ii, 0) + 1
        count = 0
        for ii in d:
            if count % 2 == 0 and d[ii] % 2 == 1:
                count += 1
            count += (d[ii] // 2) * 2
        return count



def main():
    s = Solution()
    s1 = "abccccdd"
    print(s.longestPalindrome(s1))

    s1 = "a"
    print(s.longestPalindrome(s1))

    s1 = "bb"
    print(s.longestPalindrome(s1))

    s1 = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print(s.longestPalindrome(s1))

    return



if __name__ == '__main__':
    main()
