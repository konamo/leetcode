import heapq


class Solution:
    def kClosest2(self, points: list[list[int]], k: int) -> list[list[int]]:
        d = []
        for x, y in points:
            distance = x * x + y * y
            d.append([distance, [x, y]])

        d.sort(key=lambda x: x[0])
        print(d)

        ret = []
        for ii in range(k):
            ret.append(d[ii][1])
        return ret

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        d = []
        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(d, [distance, [x, y]])

        return [ii[1] for ii in heapq.nsmallest(k, d)]

    def kClosest3(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = [x * x + y * y for x, y in points]
        low = 0
        high = max(distances)
        remaining = [ii for ii in range(len(points))]

        closest = []
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                remaining = closer
                high = mid
            else:
                remaining = farther
                low = mid
                k -= len(closer)
                closest += closer

        return [points[ii] for ii in closest]


    def split_distances(self, remaining, distances, mid):
        closer = []
        farther = []
        for ii in remaining:
            if distances[ii] <= mid:
                closer.append(ii)
            else:
                farther.append(ii)
        return [closer, farther]


def main():
    s = Solution()
    points = [[1,3],[-2,2]] 
    k = 1
    print(s.kClosest4(points, k))

    points = [[3,3],[5,-1],[-2,4]] 
    k = 2
    print(s.kClosest4(points, k))

    points = [[0,1],[1,0]]
    k = 2
    print(s.kClosest4(points, k))

    points = [[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]]
    k = 5
    print(s.kClosest4(points, k))

    return



if __name__ == '__main__':
    main()
