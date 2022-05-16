typedef struct pair_s
{
    int index;
    int value;
} pair_t;

int mycompare (const void *a, const void *b)
{
    pair_t *x = a;
    pair_t *y = b;

    return x->value - y->value;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    int *ret = (int*)malloc(sizeof(int) * 2);
    int left = 0;
    int right = numsSize - 1;
    pair_t pair[numsSize];
    *returnSize = 2;

    for (int ii = 0; ii < numsSize; ii++) {
        pair[ii].index = ii;
        pair[ii].value = nums[ii];
    }

    qsort(pair, numsSize, sizeof(pair_t), mycompare);

    while (left < right) {
        if (pair[left].value + pair[right].value == target) {
            break;;
        } else if (pair[left].value + pair[right].value < target) {
            left++;
        } else {
            right--;
        }
    }

    ret[0] = pair[left].index;
    ret[1] = pair[right].index;
    return ret;
}
