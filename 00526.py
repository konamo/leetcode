class Solution:
    def countArrangement5(self, n: int) -> int:
        if n == 1:
            return n

        nums = [ii for ii in range(1, n + 1)]
        nums = self.permutation(nums, n)

        ans = 0
        for ii in nums:
            if self.valid(ii):
                ans += 1

        return ans



    def valid(self, l: list[int]):
        for index, ii in enumerate(l):
            if ii % (index + 1) == 0 or (index + 1) % ii == 0:
                continue
            else:
                return False
        return True

    def countArrangement3(self, n: int) -> int:
        nums = [ii for ii in range(1, n + 1)]
        ret = []

        def dfs(nums: list, l: int = 1):
            if l == n and self.valid(nums):
                ret.append(nums.copy())

            for ii in range(l, n):
                nums[ii], nums[l] = nums[l], nums[ii]
                dfs(nums, l + 1)
                nums[ii], nums[l] = nums[l], nums[ii]

        dfs(nums)
        print(ret)
        return len(ret)

    def permutation(self, list1, n):
        # If the length of list=0 no permuataions possible
        if len(list1) == 0:
            return []
        # If the length of list=1, return that element
        if len(list1) == 1:
            return [list1]
        l = []
        for i in range(len(list1)):
            m = list1[i]

            if m % (n - len(list1) + 1) != 0 and (n - len(list1) + 1) % m != 0:
                continue

            # Extract list1[i] or m from the list. remlist1 is remaining list
            remlist1 = list1[:i] + list1[i+1:]
            # Generating all permutations where m is first element
            for p in self.permutation(remlist1, n):
                l.append([m] + p)
        return l


    def countArrangement(self, n: int) -> int:
        if n == 1:
            return n

        visited = [False] * (n + 1)
        count = 0
        def dfs(pos):
            nonlocal count

            if pos > n:
                count += 1
            for ii in range(1, n + 1):
                if not visited[ii] and (pos % ii == 0 or ii % pos == 0):
                    visited[ii] = True
                    dfs(pos + 1)
                    visited[ii] = False

        dfs(1)
        return count


    def permutation2(self, n):
        visited = [False] * (n + 1)

        l = []
        def dfs():
            if len(l) == n:
                print(l)
                return
            for ii in range(1, n + 1):
                if not visited[ii]:
                    visited[ii] = True
                    l.append(ii)
                    dfs()
                    visited[ii] = False
                    l.pop()
        dfs()
        return


def main():
    s = Solution()
    n = 1
    #print("1: " + str(s.countArrangement(n)))

    n = 2
    #print("2: " + str(s.countArrangement(n)))

    n = 3
    print("3: " + str(s.countArrangement(n)))

    s.permutation2(3)
    return



if __name__ == '__main__':
    main()
