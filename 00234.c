// solution 1, O(n) space
int stack[1000000];
bool isPalindrome(struct ListNode* head){
    int index = 0;
    int left, right;

    while (head) {
        stack[index++] = head->val;
        head = head->next;
    }

    left = 0;
    right = index - 1;

    while (left < right) {
        if (stack[left] == stack[right]) {
            left++;
            right--;
        } else {
            return false;
        }
    }

    return true;
}





// solution 2
typedef struct ListNode *Node;

bool isPalindrome(Node head);
void reverseTill(Node head,
                 int k,
                 Node *left_head_ptr,
                 Node *right_head_ptr);
void repairList(Node left_head, Node right_head);
int length(Node head);

bool isPalindrome(Node head) {
    // get the length of the list
    int n = length(head);

    Node left_head;
    Node right_head;

    reverseTill(head, n / 2, &left_head, &right_head);
    Node L = left_head;
    Node R = right_head;

    // skip the middle one if the total length is odd
    if (n % 2 == 1) {
        R = R->next;
    }

    while (L || R) {
        if (L->val != R->val) {
            // repair the list probably not necessary
            repairList(left_head, right_head);
            return false;
        }
        L = L->next;
        R = R->next;
    }

    // repair the list probably not necessary
    repairList(left_head, right_head);
    return true;
}

void reverseTill(Node head, int k, Node *left_head_ptr, Node *right_head_ptr) {
    Node previous = NULL;
    for (int i = 0; i < k && head; i++) {
        Node temp = head->next;
        head->next = previous;
        previous = head;
        head = temp;
    }
    *left_head_ptr = previous;
    *right_head_ptr = head;
}

void repairList(Node left_head, Node right_head)
{
    while (left_head) {
        Node temp = left_head->next;

        left_head->next = right_head;
        right_head = left_head;
        left_head = temp;
    }
}



int length (Node head)
{
    int count;

    while (head) {
        head = head->next;
        count++;
    }

    return count;
}


// solution 3 (based on solution 2) with optimization
bool isPalindrome(struct ListNode* head)
{
    struct ListNode *slow, *fast;
    struct ListNode *next, *prev;
    struct ListNode *L, *R;

    slow = head;
    fast = head;
    prev = NULL;
    while (fast && fast->next) {
        fast = fast->next->next;

        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    // skip the middle one if necessary
    if (fast == NULL) {
        L = prev;
        R = slow;
    } else {
        L = prev;
        R = slow->next;
    }

    while (L && R) {
        if (L->val == R->val) {
            L = L->next;
            R = R->next;
        } else {
            return false;
        }
    }

    return true;
}
