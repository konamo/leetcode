class Solution:
    def mySqrt2(self, x: int) -> int:
        ii = 1
        while True:
            if ii * ii > x:
                return ii - 1
            elif ii * ii == x:
                return ii
            else:
                ii += 1

        return

    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1

def main():
    s = Solution()
    x = 4
    print(s.mySqrt(x))

    x = 8
    print(s.mySqrt(x))
    return 


if __name__ == '__main__':
    main()
