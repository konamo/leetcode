class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ii = 0
        jj = ii + 1

        while jj < len(nums):
            if nums[jj] != nums[jj - 1]:
                ii += 1
                nums[ii] = nums[jj]
                jj += 1
            else:
                jj += 1
        return ii + 1



def main():
    s = Solution()
    nums = [1,1,2]
    print(s.removeDuplicates(nums))

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))



    return



if __name__ == '__main__':
    main()
