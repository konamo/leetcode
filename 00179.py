class LargerNumKey(str):
    def __lt__(x, y):
        return str(x) + str(y) > str(y) + str(x)


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums.sort(key = LargerNumKey)


        return ''.join([str(i) for i in nums]) if nums[0] else '0'
            


def main():
    s = Solution()
    nums = [3,30,34,5,9]
    print("1: " + s.largestNumber(nums))

    nums = [0]
    print("1: " + s.largestNumber(nums))
    return



if __name__ == '__main__':
    main()
