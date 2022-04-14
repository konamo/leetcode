from sortedcontainers import SortedDict



class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dic[key]
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if timestamp < arr[mid][0]:
                right = mid - 1
            elif timestamp > arr[mid][0]:
                left = mid + 1
            else:
                return arr[mid][1]

        return arr[right][1] if right >= 0 else ""
