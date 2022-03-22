class Solution:
    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        # dfs doesn't work, see test case 4
        found = False
        bag = [False] * len(nums)
        ans = []
        def dfs():
            nonlocal found
            nonlocal ans


            if found:
                return

            s = sum([nums[ii] for ii in range(len(nums)) if bag[ii] == True])

            if target == s:
                found = True
                ans += [ii for ii in range(len(nums)) if bag[ii] == True]
                return

            for ii in range(len(nums)):
                if bag[ii] == False:
                    bag[ii] = True
                    dfs()
                    bag[ii] = False

            return



        for ii in range(len(nums)):
            if found:
                break
            bag[ii] = True
            dfs()
            bag[ii] = False

        return ans


    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for ii, val in enumerate(nums):
            if val in d:
                return [d[val], ii]
            else:
                d[target - val] = ii
        arr = []
        for i, x in enumerate(nums):
            arr.append([x, i])
        arr.sort()  # Sort arr in increasing order by their values.
        
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = []
        for i, x in enumerate(nums):
            arr.append([x, i])
        arr.sort()

        left, right = 0, len(arr) - 1
        while left < right:
            sum2 = arr[left][0] + arr[right][0]
            if sum2 == target:
                return [arr[left][1], arr[right][1]]
            elif sum2 > target:
                right -= 1  # Try to decrease sum2
            else:
                left += 1  # Try to increase sum2

def main():
    s = Solution()

    nums = [2,7,11,15]
    target = 9
    print("1: " + str(s.twoSum(nums, target)))

    nums = [3,2,4]
    target = 6
    print("2: " + str(s.twoSum(nums, target)))

    nums = [3,3]
    target = 6
    print("3: " + str(s.twoSum(nums, target)))


    nums = [0,4,3,0]
    target = 0
    print("4: " + str(s.twoSum(nums, target)))
    return


if __name__ == '__main__':
    main()
