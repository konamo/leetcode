struct ListNode* removeElements(struct ListNode* head, int val)
{
    struct ListNode dummy;
    struct ListNode *prev;


    dummy.next = head;
    prev = &dummy;
    while (head) {
        if (head->val == val) {
            prev->next = head->next;
            free(head);
        } else {
            prev = head;
        }
        head = prev->next;
    }


    return dummy.next;
}
