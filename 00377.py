class Solution:
    def combinationSum41(self, nums: list[int], target: int) -> int:
        ans = []
        def dfs(ret):

            if sum(ret) == target:
                ans.append(ret[:])
            elif sum(ret) > target:
                return

            for ii in nums:
                ret.append(ii)
                dfs(ret)
                ret.pop()

        dfs([])
        return len(ans)

    def combinationSum4(self, nums, target):
        # DP
        # the nums need to be sorted first
        # build up combs from lowest
        nums, combs = sorted(nums), [0] * (target + 1)
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                elif num == i:
                    combs[i] += 1
                elif num < i:
                    combs[i] += combs[i - num]
        return combs[target]


def main():
    s = Solution()
    nums = [1,2,3]
    target = 4
    print(s.combinationSum4(nums, target))

    nums = [9]
    target = 3
    print(s.combinationSum4(nums, target))

    nums = [4,2,1]
    target = 32
    print(s.combinationSum4(nums, target))

    return



if __name__ == '__main__':
    main()
