class Solution:
    def reorganizeString2(self, s: str) -> str:
        res, c = [], Counter(s)
        pq = [(-value,key) for key,value in c.items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        res = ''.join(res)
        if len(res) != len(s): return ""
        return res


    def reorganizeString(self, s: str) -> str:
        # a = sorted(sorted(s), key=s.count)
        a = sorted(s, key=lambda x: (-s.count(x), x))
        h = (len(a) + 1) // 2
        a[1::2], a[::2] = a[h:], a[:h]
        return ''.join(a) * (a[0] != a[1])



def main():
    s = Solution()
    s1 = "aab"
    print(s.reorganizeString(s1))

    s1 = "aaab"
    print(s.reorganizeString(s1))

    s1 = "abbabbaaab"
    print(s.reorganizeString(s1))
    return


if __name__ == '__main__':
    main()
