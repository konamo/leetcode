#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # print value in order
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


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        a = []
        while head:
            a.append(head.val)
            head = head.next

        b = []
        l = ListNode()
        t = l
        for ii in a:
            if ii not in b:
                l.next = ListNode(ii)
                l = l.next
                b.append(ii)

        return t.next

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        curr = head.next
        prev = head

        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return head





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

def main():
    l = ListNode(1)
    ListAppendNode(l, ListNode(1))
    ListAppendNode(l, ListNode(2))
    ListAppendNode(l, ListNode(3))
    ListAppendNode(l, ListNode(3))

    s = Solution()
    l = s.deleteDuplicates2(l)
    l.printval()
    return


if __name__ == '__main__':
    main()
