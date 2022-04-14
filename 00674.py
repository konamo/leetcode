class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for ii in range(1, len(nums)):
            if nums[ii] > nums[ii-1]:
                dp[ii] = dp[ii-1]+1

        return max(dp)

    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: 
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans





def main():
    s = Solution()
    nums = [1,3,5,4,7] 
    print(s.findLengthOfLCIS(nums))


    nums = [2,2,2,2,2]
    print(s.findLengthOfLCIS(nums))
    return 


if __name__ == '__main__':
    main()
