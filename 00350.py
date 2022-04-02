class Solution:
    def intersect2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        d2 = {}
        ret = []
        for ii in nums1:
            d[ii] = d.get(ii, 0) + 1
        for ii in nums2:
            d2[ii] = d2.get(ii, 0) + 1

        for ii in d:
            if ii in d2:
                count = min(d[ii], d2[ii])
                ret += [ii] * count

            
        return ret

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        ret = []
        for ii in nums1:
            d[ii] = d.get(ii, 0) + 1

        for ii in nums2:
            if ii in d:
                ret.append(ii)
                d[ii] = d.get(ii) - 1
                if d[ii] == 0:
                    del d[ii]

            
        return ret

    def intersect3(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans

    def intersect4(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()


        ret = []
        ii = 0
        jj = 0
        
        while ii < len(nums1) and jj < len(nums2):
            if nums1[ii] == nums2[jj]:
                ret.append(nums1[ii])
                ii += 1
                jj += 1
            elif nums1[ii] < nums2[jj]:
                ii += 1
            elif nums1[ii] > nums2[jj]:
                jj += 1

        return ret




def main():
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(s.intersect4(nums1, nums2))


    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(s.intersect4(nums1, nums2))
    return



if __name__ == '__main__':
    main()
