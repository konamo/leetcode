/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// two pass solution
struct ListNode* removeNthFromEnd (struct ListNode* head, int n) {
    struct ListNode dummy;
    struct ListNode *prev;
    int count = 0;
    int ii;

    dummy.next = head;

    while (head) {
        head = head->next;
        count++;
    }

    head = dummy.next;
    prev = &dummy;
    for (ii = 0; ii < count - n; ii++) {
        prev = head;
        head = head->next;
    }
    prev->next = head->next;

    return dummy.next;
}

// one pass solution
// two points, n distance to each other
// as long as the first one reaches the end of the list
// the first needs to be removed
struct ListNode* removeNthFromEnd (struct ListNode* head, int n) {
    struct ListNode dummy;
    struct ListNode *first, *second;


    dummy.next = head;

    // n distance between first and second
    first = head;
    while (n) {
        first = first->next;
        n--;
    }
    second = &dummy;

    // as long as first reaches the NULL, second is one node before the remove node
    while (first) {
        first = first->next;
        second = second->next;
    }
    second->next = second->next->next;

    return dummy.next;
}
