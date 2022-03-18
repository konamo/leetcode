from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddDummy = oddCurr = ListNode()
        evenDummy = evenCurr = ListNode()


        step = 1
        while head:
            if step % 2:
                oddCurr.next = head
                oddCurr = head
            else:
                evenCurr.next = head
                evenCurr = head
            head = head.next
            step += 1
        evenCurr.next = None
        oddCurr.next = evenDummy.next


        return oddDummy.next

    def printList(self, head):
        while head:
            print(head.val, end = '->')
            head = head.next
        print("None")



def main():
    s = Solution()
    a = ListNode(5)
    b = ListNode(4, a)
    c = ListNode(3, b)
    d = ListNode(2, c)
    e = ListNode(1, d)
    f = s.oddEvenList(e)
    s.printList(f)

    return



if __name__ == '__main__':
    main()
