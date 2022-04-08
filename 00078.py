class Solution:
    def subsets2(self, nums: list[int]) -> list[list[int]]:
        ret = []
        ans = []
        def dfs(nums):
            ans.append(ret.copy())

            for index, ii in enumerate(nums):
                ret.append(ii)
                dfs(nums[index+1:])
                ret.pop()

        dfs(nums)
        return ans

    def subsets3(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
            print(output)
        
        return output



    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return

            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

        n = len(nums)
        output = []
        
    def subsets5(self, nums: list[int]) -> list[list[int]]:
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output




def main():
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))

    nums = [0]
    print(s.subsets(nums))
    return



if __name__ == '__main__':
    main()
