# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
       
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListInt(head, newHead):
            if not head:
                return newHead

            next = head.next
            head.next = newHead
            return reverseListInt(next, head)

        return reverseListInt(head, None)

