from collections import Counter
import heapq

class Solution:
    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for ii in nums:
            d[ii] = d.get(ii, 0) + 1

        ret = []
        for ii in d:
            ret.append([ii, d[ii]])
        ret.sort(reverse=True, key=lambda x: x[1])
        return [ret[ii][0] for ii in range(k)]


    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        print(count.keys())
        return heapq.nlargest(k, count.keys(), key=count.get)


def main():
    s = Solution()
    nums = [1,1,1,2,2,3,4]
    k = 2
    print(s.topKFrequent(nums, k))

    nums = [1]
    k = 1
    print(s.topKFrequent(nums, k))
    return



if __name__ == '__main__':
    main()
