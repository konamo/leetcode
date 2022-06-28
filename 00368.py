class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        # make sure nums are unique, otherwise this algorithm doesn't work
        assert(len(set(nums)) == len(nums))

        # sort list first
        nums.sort()

        # dp[x][0] is the index to the previous element
        # dp[x][1] is how many elements so far in the group
        dp = [[0, 1] for _ in range(len(nums))]
        m = 0 # max number elements
        ind = 0 # last element index

        for index, value in enumerate(nums):
            dp[index][0] = index # use index == dp[index][0] as a terminator
            for ii in range(index):
                # only check if nums[ii+1] % nums[ii] == 0 because:
                # 1. the list is sorted
                # 2. all nums are unique
                if value % nums[ii] == 0:
                    if dp[ii][1] >= dp[index][1]:
                        dp[index][0] = ii
                        dp[index][1] = dp[ii][1] + 1
            
            # keep track of the max elements group so far
            if dp[index][1] > m:
                m = dp[index][1]
                ind = index

        # add elements to the return list
        # from the last element to the first
        ret = []
        while ind != dp[ind][0]:
            ret.append(nums[ind])
            ind = dp[ind][0]

        ret.append(nums[ind])

        return ret






def main():
    s = Solution()

    nums = [3, 2, 1]
    print(s.largestDivisibleSubset(nums))

    nums = [1, 8, 4, 2]
    print(s.largestDivisibleSubset(nums))

    nums = [3, 5, 2]
    print(s.largestDivisibleSubset(nums))

    return



if __name__ == '__main__':
    main()
