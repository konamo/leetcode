from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        step = 1
        prev = None
        curr = head
        while step < left:
            prev = curr
            curr = curr.next
            step += 1
        
        
        def reverse(head):
            nonlocal right
            nonlocal step
            
            prev = None
            curr = head
            
            while step <= right:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                step += 1
            head.next = next
            return prev

        newHead = reverse(curr)
        if prev:
            prev.next = newHead
        else:
            head = newHead
        
        return head
    
    def printList(self, head):
        while head:
            print(head.val, end = '->')
            head = head.next
        print("None")

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left = right = head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, m, n)
        return head

    def reverseBetween3(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


def main():
    a = ListNode(5)
    b = ListNode(4, a)
    c = ListNode(3, b)
    d = ListNode(2, c)
    e = ListNode(1, d)
    s = Solution()
    s.printList(e)
    print("left = " + str(2))
    print("right = " + str(4))
    h = s.reverseBetween(e, 2, 4)
    s.printList(h)
    print()


    h = s.reverseBetween(a, 1, 1)
    s.printList(h)

    a = ListNode(5)
    b = ListNode(3, a)
    h = s.reverseBetween(b, 1, 2)
    s.printList(h)

    return


if __name__ == '__main__':
    main()
