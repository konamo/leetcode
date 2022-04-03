class Solution:
    def nthUglyNumber2(self, n: int) -> int:
        x = 1
        ans = []
        while n > 0:
            if self.isUgly(x):
                ans.append(x)
                n -= 1
            x += 1
        return ans[-1]

    def isUgly(self, x):
        while x % 2 == 0:
            x //= 2
        while x % 3 == 0:
            x //= 3
        while x % 5 == 0:
            x //= 5
        if x == 1:
            return True
        else:
            return False

    def nthUglyNumber3(self, n: int) -> int:
        ans = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            u2, u3, u5 = 2 * ans[i2], 3 * ans[i3], 5 * ans[i5]
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ans.append(umin)
            n -= 1
        return ans[-1]

    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        k = len(factors)
        starts = [0] * k
        ans = [1]
        while n > 1:
            candidates = [factors[ii] * ans[starts[ii]] for ii in range(k)]
            new_num = min(candidates)
            ans.append(new_num)
            starts = [starts[ii] + (candidates[ii] == new_num) for ii in range(k)]
            n -= 1
        return ans[-1]


def main():
    s = Solution()
    n = 10
    print(s.nthUglyNumber(n))

    n = 420
    print(s.nthUglyNumber(n))
    return



if __name__ == '__main__':
    main()
