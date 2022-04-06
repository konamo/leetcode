class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
	
        def kSum(nums: list[int], target: int, k: int) -> list[list[int]]:
            res = []
            
            # If we have run out of numbers to add, return res.
            if not nums:
                return res
            
            # There are k remaining values to add to the sum. The 
            # average of these values is at least target // k.
            average_value = target // k
            
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest 
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            if k == 2:
                return twoSum(nums, target)
    
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
    
            return res

        def twoSum(nums: list[int], target: int) -> list[list[int]]:
            # two pointers

            res = []
            lo, hi = 0, len(nums) - 1
    
            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                                                         
            return res


        def twoSum(nums: list[int], target: int) -> list[list[int]]:
            # hashmap
            res = []
            s = set()
    
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
    
            return res

        nums.sort()
        return kSum(nums, target, 4)

def main():
    s = Solution()
    nums = [1,0,-1,0,-2,2] 
    target = 0 
    print(s.fourSum(nums, target))
    
    nums = [2,2,2,2,2]
    target = 8
    print(s.fourSum(nums, target))
    return



if __name__ == '__main__':
    main()
