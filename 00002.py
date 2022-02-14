# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    # print value in reverse order
    def printval(self):
        s = self
        while s != None:
            print(s.val, end = '')
            s = s.next
        print()

    # return the actual value
    def output(self):
        s = self
        val = 0
        i = 0
        while s != None:
            val += s.val * pow(10, i)
            i += 1
            s = s.next
        return val


def ListAppendNode(l, next):
    """
    l: the first ListNode of a list
    next: a ListNode to be appended at the end
    return None
    """
    if l == None:
        # this is an error case
        return

    while l.next != None:
        l = l.next
    l.next = next
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        head = l3
        carry = 0

        while l1 != None or l2 != None:
            x = 0
            y = 0

            if l1 != None:
                x = l1.val
                l1 = l1.next

            if l2 != None:
                y = l2.val
                l2 = l2.next

            l3.next = ListNode((x + y + carry) % 10)
            carry = (x + y + carry) // 10
            l3 = l3.next

        if carry != 0:
            l3.next = ListNode(carry)

        return head.next


def main():
    s = Solution()
    l1 = ListNode(6, ListNode(7))
    l2 = ListNode(4, ListNode(3))
    l3 = s.addTwoNumbers(l1, l2)
    assert 110 == l3.output()

    l1 = ListNode(3)
    l2 = ListNode(4)
    l3 = s.addTwoNumbers(l1, l2)
    assert 7 == l3.output()

    l1 = ListNode(3, ListNode(2))
    l2 = ListNode(4, ListNode(3))
    l3 = s.addTwoNumbers(l1, l2)
    assert 57 == l3.output()

    l1 = ListNode(3)
    l2 = ListNode(4, ListNode(3))
    l3 = s.addTwoNumbers(l1, l2)
    assert 37 == l3.output()

    l1 = ListNode(3, ListNode(4))
    l2 = ListNode(4)
    l3 = s.addTwoNumbers(l1, l2)
    assert 47 == l3.output()

    l1 = ListNode(3, ListNode(4))
    l2 = ListNode(8)
    l3 = s.addTwoNumbers(l1, l2)
    assert 51 == l3.output()

    print('Pass')

if __name__ == "__main__":
    main()
