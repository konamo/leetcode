class Solution:
    def isPalindrome2(self, s: str) -> bool:
        new = []
        for ii in s:
            if 'a' <= ii <= 'z':
                new.append(ii)
            elif '0' <= ii <= '9':
                new.append(ii)
            elif 'A' <= ii <= 'Z':
                new.append(ii.lower())
            else:
                pass
        new1 = new.copy()
        new.reverse()
        if new1 == new:
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

def main():
    s = Solution()
    s1 = "A man, a plan, a canal: Panama" 
    print(s.isPalindrome(s1))


    s1 = "race a car"
    print(s.isPalindrome(s1))


    s1 = " "
    print(s.isPalindrome(s1))
    return




if __name__ == '__main__':
    main()
