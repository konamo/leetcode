class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if target < nums[0] < nums[M]: # -inf
                L = M+1
            elif target >= nums[0] > nums[M]: # +inf
                H = M
            elif nums[M] < target:
                L = M+1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1


def main():
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums, target))

    nums = [4,5,6,7,0,1,2]
    target = 3
    print(s.search(nums, target))

    nums = [1]
    target = 0
    print(s.search(nums, target))

    return



if __name__ == '__main__':
    main()
