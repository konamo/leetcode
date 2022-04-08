class Solution:
    def maxSubArray2(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def maxSubArray3(self, nums: list[int]) -> int:
        m = float('-inf')
        s = 0
        for ii in range(len(nums)):
            if s < 0:
                s = nums[ii] 
            else:
                nums[ii] += s 
                s = nums[ii]
            m = max(m, s)

        return m

    def maxSubArray(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)


def main():
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))

    nums = [1]
    print(s.maxSubArray(nums))
    
    nums = [5,4,-1,7,8]
    print(s.maxSubArray(nums))

    nums = [-1]
    print(s.maxSubArray(nums))

    nums = [-2,-1]
    print(s.maxSubArray(nums))
    
    return




if __name__ == '__main__':
    main()
