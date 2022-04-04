import heapq


class Solution:
    def kthSmallest2(self, matrix: list[list[int]], k: int) -> int:
        l = []
        for ii in range(len(matrix)):
            l += matrix[ii]
        l.sort()
        return l[k - 1]

    def kthSmallest3(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heap = []
        for ii in range(m):
            for jj in range(n):
                if len(heap) == m * n - k + 1:
                    if matrix[ii][jj] > heap[0]:
                        heapq.heappushpop(heap, matrix[ii][jj])
                else:
                    heapq.heappush(heap, matrix[ii][jj])

        return heap[0]

    def kthSmallest4(self, matrix: list[list[int]], k: int) -> int:
        l = []
        for ii in range(len(matrix)):
            l += matrix[ii]
        heapq.heapify(l)
        while k > 0:
            ret = heapq.heappop(l)
            k -= 1
        return ret

    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        p = [0] * m
        while True:
            c = float("inf")
            for ii in range(m):
                if p[ii] < n:
                    c = min(matrix[ii][p[ii]], c)
            for ii in range(m):
                if p[ii] < n:
                    if c == matrix[ii][p[ii]]:
                        p[ii] += 1
                        break
            k -= 1
            if k == 0:
                break
        return c






def main():
    s = Solution()
    matrix = [[1,5,9],[10,11,13],[12,13,15]] 
    k = 8
    print(s.kthSmallest(matrix, k))

    matrix = [[-5]]
    k = 1
    print(s.kthSmallest(matrix, k))
    return




if __name__ == '__main__':
    main()
