class Solution:
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1
        return



def main():
    s = Solution()
    numbers = [2,7,11,15] 
    target = 9
    print(s.twoSum(numbers, target))

    numbers = [2,3,4] 
    target = 6
    print(s.twoSum(numbers, target))

    numbers = [-1,0] 
    target = -1
    print(s.twoSum(numbers, target))

    return



if __name__ == '__main__':
    main()
