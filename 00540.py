from functools import reduce


class Solution:
    def singleNonDuplicate2(self, nums: list[int]) -> int:
        s = [ii for ii in nums if nums.count(ii) == 1]
        return s[0]

    def singleNonDuplicate3(self, nums: list[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1 and nums[mid - 1] == nums[mid]:
                left = mid + 1
            elif mid % 2 == 0 and nums[mid + 1] == nums[mid]:
                left = mid + 2
            else:
                right = mid
        assert(left == right)
        return nums[left]
    
    def singleNonDuplicate4(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

    def singleNonDuplicate(self, nums):
        return reduce(lambda x, y: x ^ y, nums)


def main():
    s = Solution()
    nums = [1,1,2,3,3,4,4,8,8]
    print(s.singleNonDuplicate(nums))

    nums = [3,3,7,7,10,11,11]
    print(s.singleNonDuplicate(nums))
    return



if __name__ == '__main__':
    main()
