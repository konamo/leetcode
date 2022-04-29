struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode *curr, *next;

    curr = head;

    while (curr && curr->next) {
        next = curr->next;
        if (next->val == curr->val) {
            curr->next = next->next;
            free(next);
        } else {
            curr = curr->next;
        }
    }

    return head;
}
