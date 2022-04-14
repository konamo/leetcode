class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for ii in range(2, n+1):
            dp[ii] = dp[ii-1] + dp[ii-2]

        return dp[n]



def main():
    s = Solution()
    n = 
    print(s.climbStairs(n))
    return



if __name__ == '__main__':
    main()
