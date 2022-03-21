class Solution:
    def removeDuplicates2(self, s: str, k: int) -> str:
        top = -1
        jj = 0
        stack = []
        for ii in s:
            if ii == top and jj + 1 == k:
                while jj:
                    stack.pop()
                    jj -= 1
                assert(jj == 0)

                if stack:
                    top = stack[-1]
                    jj = 1
                    kk = -2
                    while True:
                        if len(stack) + kk >= 0 and top == stack[kk]:
                            jj += 1
                            kk -= 1
                        else:
                            break

            elif ii == top:
                stack.append(ii)
                jj += 1
            else:
                stack.append(ii)
                top = ii
                jj = 1

        return ''.join(stack)

    def removeDuplicates3(self, s: str, k: int) -> str:
        stack = []
        for ii in s:
            if stack:
                if ii == stack[-1][0]:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([ii, 1])
            else:
                stack.append([ii, 1])

        return ''.join(ii[0] * ii[1] for ii in stack)

    def removeDuplicates(self, s: str, k: int) -> str:
        ii = 0
        n = len(s)
        count = [None] * n
        jj = 0
        list1 = list(s)
        while jj < n:
            list1[ii] = list1[jj]
            if ii > 0 and list1[ii - 1] == list1[ii]:
                count[ii] = count[ii - 1] + 1
            else:
                count[ii] = 1
            if count[ii] == k:
                ii -= k
            jj += 1
            ii += 1
        return ''.join(list1[:ii])


def main():
    s = Solution()
    s1 = "abcd"
    k = 2
    print("1: " + s.removeDuplicates(s1, k))

    s1 = "deeedbbcccbdaa"
    k = 3
    print("2: " + s.removeDuplicates(s1, k))


    s1 = "pbbcggttciiippooaais"
    k = 2
    print("3: " + s.removeDuplicates(s1, k))

    s1 = "deeedbbcccbdaa"
    k = 3
    print("4: " + s.removeDuplicates(s1, k))
    
    return




if __name__ == '__main__':
    main()
