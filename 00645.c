int* findErrorNums (int* nums, int numsSize, int* returnSize)
{
    int *ret = (int*)malloc(sizeof(int) * 2);


    for (int ii = 0; ii < numsSize; ii++) {
        if (nums[abs(nums[ii]) - 1] < 0) {
            ret[0] = abs(nums[ii]);
        } else {
            nums[abs(nums[ii]) - 1] *= -1;
        }
    }

    for (int ii = 0; ii < numsSize; ii++) {
        if (nums[ii] > 0) {
            ret[1] = ii + 1;
            break;
        }
    }

    *returnSize = 2;
    return ret;
}



int* findErrorNums (int* nums, int numsSize, int* returnSize)
{
    int *ret = (int*)malloc(sizeof(int) * 2);
    int p = 0, acc1 = 0, acc2 = 0;

    // Get the xor of missing and duplicate numbers
    for (int i = 0; i < numsSize; ++i)
        p ^= (i + 1) ^ nums[i];

    p &= ~(p - 1); // We'll use only the last significant set bit

    // Split the numbers in 2 categories and xor them
    for (int i = 0; i < numsSize; ++i) {
        if ((nums[i] & p) == 0) {
            acc1 ^= nums[i];
        } else {
            acc2 ^= nums[i];
        }

        if (((i + 1) & p) == 0) {
            acc1 ^= i + 1;
        } else {
            acc2 ^= i + 1;
        }
    }

    *returnSize = 2;
    // Determine which is the duplicate number
    for (int ii = 0; ii < numsSize; ii++) {
        if (nums[ii] == acc1) {
            ret[0] = acc1;
            ret[1] = acc2;
            return ret;
        }
    }
    ret[0] = acc2;
    ret[1] = acc1;
    return ret;
}
