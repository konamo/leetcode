class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ret = ''
        for ii in s:
            if ii == ']':
                r = []
                while True:
                    t = stack.pop()
                    if t == '[':
                        n = 0
                        ii = 1
                        while stack:
                            n1 = stack.pop()
                            if '0' <= n1 <= '9':
                                n += int(n1) * ii
                                ii *= 10
                            else:
                                stack.append(str(n1))
                                break

                        for ii in range(len(r) * int(n)):
                            stack.append(r[ii % len(r)])
                        break
                    else:
                        r.insert(0, t)
            else:
                stack.append(ii)

        while stack:
            ret += stack.pop(0)
        return ret


    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString


def main():
    s = Solution()
    s1 = "3[a]2[bc]" 
    print(s.decodeString(s1))


    s1 = "3[a2[c]]"
    print(s.decodeString(s1))

    s1 = "2[abc]3[cd]ef"
    print(s.decodeString(s1))

    s1 = "100[leetcode]"
    print(s.decodeString(s1))
    return



if __name__ == '__main__':
    main()
