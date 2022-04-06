class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ii = jj = 0
        target = 0

        for jj in range(len(nums)):
            if nums[jj] == target:
                continue
            else:
                nums[ii], nums[jj] = nums[jj], nums[ii]
                ii += 1
            
        return nums


def main():
    s = Solution()
    nums = [0,1,0,3,12] 
    print(s.moveZeroes(nums))

    nums = [0]
    print(s.moveZeroes(nums))
    return




if __name__ == '__main__':
    main()
