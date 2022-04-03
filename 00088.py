class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # left to right is pretty hard
        # we can do right to left
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2
        return nums1.sort()




def main():
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1,0]
    m = 1
    nums2 = [2]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [4,0,0,0,0,0]
    m = 1
    nums2 = [1,2,3,5,6]
    n = 5
    s.merge(nums1, m, nums2, n)
    print(nums1)
    
    nums1 = [1,2,4,5,6,0]
    m = 5
    nums2 = [3]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    return



if __name__ == '__main__':
    main()
