class Solution:
    def minRemoveToMakeValid2(self, s: str) -> str:
        list1 = list(s)
        list2 = []
        count = 0
        for ii, l in enumerate(list1):
            if l == '(':
                count += 1
            elif l == ')':
                count -= 1

            if count < 0:
                count = 0
            else:
                list2.append(l)
        
        list1 = []
        for ii in range(len(list2) - 1, -1, -1):
            if list2[ii] == '(' and count > 0:
                count -= 1
            else:
                list1.insert(0, list2[ii])
        return ''.join(list1)


    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for ii, char in enumerate(s):
            if char == '(':
                stack.append(ii)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[ii] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)

def main():
    s = Solution()
    s1 = "lee(t(c)o)de)"
    print("1: " + s.minRemoveToMakeValid(s1))


    s1 = "a)b(c)d"
    print("2: " + s.minRemoveToMakeValid(s1))

    s1 = "))(("
    print("3: " + s.minRemoveToMakeValid(s1))
    return



if __name__ == '__main__':
    main()
