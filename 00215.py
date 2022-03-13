import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # heap solution
        n = len(nums)
        if n < k:
            return

        q = nums[:k]
        heapq.heapify(q)

        for ii in range(k, n):
            if nums[ii] > q[0]:
                heapq.heappushpop(q, nums[ii])

        return q[0]

    def findKthLargest2(self, nums: list[int], k: int) -> int:
        # convert kth largest (1-based) to kth smallest (0-based)
        k = len(nums) - k

        def partition(low, high):
            if low == high:
                return low
            elif low > high:
                print("something wrong!")
            else:
                # pick first element as pivot
                ii = low + 1
                jj = high

                while True:
                    while ii <= high and nums[ii] < nums[low]:
                        ii += 1
                    while jj >= low and nums[jj] > nums[low]:
                        jj -= 1
                    if ii >= jj:
                        break
                    
                    nums[ii], nums[jj] = nums[jj], nums[ii]

                nums[jj], nums[low] = nums[low], nums[jj]
            return jj


        low = 0
        high = len(nums) - 1
        while low <= high:
            jj = partition(low, high)
            if jj < k:
                low = jj + 1
            elif jj > k:
                high = jj - 1
            else:
                return nums[jj]





def main():
    s = Solution()
    nums = [3,2,1,5,6,4]
    k = 3
    print("1: " + str(s.findKthLargest2(nums, k)))

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print("2: " + str(s.findKthLargest2(nums, k)))

    nums = [2,1]
    k = 1
    print("3: " + str(s.findKthLargest2(nums, k)))
    
    return



if __name__ == '__main__':
    main()
