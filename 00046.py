class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:


        length = len(nums)
        ans = []
        def dfs(nums, ret):
            if len(ret) == length:
                ans.append(ret[:])
                return

            for index, ii in enumerate(nums):
                ret.append(ii)
                dfs(nums[0:index] + nums[index+1:], ret)
                ret.pop()


            return


        dfs(nums, [])
        return ans



def main():
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))

    nums = [0,1]
    print(s.permute(nums))

    nums = [1]
    print(s.permute(nums))
    return



if __name__ == '__main__':
    main()
