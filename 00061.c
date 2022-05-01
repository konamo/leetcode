struct ListNode* rotateRight(struct ListNode* head, int k)
{
    int count = 0;
    struct ListNode *dummy = head;
    struct ListNode *next;
    struct ListNode *newHead;
    int ii;

    while (head) {
        head = head->next;
        count++;
    }

    if (count == 0) {
        return NULL;
    }

    k %= count;
    if (k == 0) {
        return dummy;
    }

    head = dummy;
    for (ii = 0; ii < count - k - 1; ii++) {
        head = head->next;
    }

    next = head->next;
    head->next = NULL;

    newHead = next;
    while (next->next) {
        next = next->next;
    }
    next->next = dummy;

    return newHead;
}
