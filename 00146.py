import collections

class LRUCache2:
    # ordered dict method
    def __init__(self, capacity: int):
        self.dict = collections.OrderedDict()
        self.cap  = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict.pop(key)
            self.dict[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
            self.dict[key] = value
        else:
            if len(self.dict) < self.cap:
                self.dict[key] = value
            else:
                self.dict.popitem(last=False)
                self.dict[key] = value
        
class ListNode:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.prev = prev
        self.next = next
        self.key  = key
        self.val  = val


class LRUCache:
    # dict + double linked list
    def __init__(self, capacity: int):
        self.dict = {}
        self.cap  = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            node.val = value
            self.add(node)
        else:
            if len(self.dict) < self.cap:
                node = ListNode(key, value)
                self.add(node)
                self.dict[key] = node
            else:
                node = ListNode(key, value)
                self.dict.pop(self.head.next.key)
                self.remove(self.head.next)
                self.add(node)
                self.dict[key] = node
    
    def remove(self, node):
        # remove node from the list
        node.prev.next = node.next
        node.next.prev = node.prev
        return

    def add(self, node):
        # add node to the tail
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
        return


def main():
    obj = LRUCache(2)
    obj.put(2, 1)
    obj.put(3, 2)
    print(obj.get(3))
    print(obj.get(2))
    obj.put(4, 3)
    print(obj.get(2))
    print(obj.get(3))
    print(obj.get(4))

    return



if __name__ == '__main__':
    main()
