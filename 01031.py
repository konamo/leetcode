class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        def maxSum(L, M):
            maxL = 0
            ans = 0
            for ii in range(M+L, len(prefixSum)):
                maxL = max(maxL, prefixSum[ii-M] - prefixSum[ii-M-L])
                ans = max(ans, maxL + prefixSum[ii] - prefixSum[ii-M])
            return ans


        prefixSum = [0] * (len(nums) + 1)
        for ii in range(len(nums)):
            prefixSum[ii+1] = prefixSum[ii] + nums[ii]

        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))


    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        def maxSum(L:int, M:int) -> int:
            sumL = sumM = 0
            for i in range(0, L + M):
                if i < L:
                    sumL += nums[i]
                else:
                    sumM += nums[i]    

            maxL, ans = sumL, sumL + sumM
            for i in range(L + M, len(A)):
                sumL += nums[i - M] - nums[i - L - M]
                maxL = max(maxL, sumL)
                sumM += nums[i] - nums[i - M]
                ans = max(ans, maxL + sumM)
            return ans
        
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))

def main():
    s = Solution()
    nums = [0,6,5,2,2,5,1,9,4]
    firstLen = 1
    secondLen = 2
    print(s.maxSumTwoNoOverlap(nums, firstLen, secondLen))

    nums = [3,8,1,3,2,1,8,9,0]
    firstLen = 3
    secondLen = 2
    print(s.maxSumTwoNoOverlap(nums, firstLen, secondLen))

    nums = [2,1,5,6,0,9,5,0,3,8]
    firstLen = 4
    secondLen = 3
    print(s.maxSumTwoNoOverlap(nums, firstLen, secondLen))



    return




if __name__ == '__main__':
    main()
