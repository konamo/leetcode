#define MAX(a, b) ((a) > (b) ? (a) : (b))

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// solution 1: brute force
int* getMaximumXor (int* nums, int numsSize, int maximumBit, int* returnSize)
{
    int *ret = (int*)malloc(sizeof(int) * numsSize);

    for (int ii = numsSize; ii > 0; ii--) {
        int maxXor = -1;
        int maxKK;
        for (int kk = 0; kk < (1ull << maximumBit); kk++) {
            int xor = 0;
            for (int jj = 0; jj < ii; jj++) {
                xor ^= nums[jj];
            }
            xor ^= kk;
            if (xor > maxXor) {
                maxXor = xor;
                maxKK = kk;
            }
        }
        ret[numsSize - ii] = maxKK;
    }

    *returnSize = numsSize;

    return ret;
}


// solution 2: to pre-calculate the XOR and reverse the XOR for k
int* getMaximumXor (int* nums, int numsSize, int maximumBit, int* returnSize)
{
    int *ret = (int*)malloc(sizeof(int) * numsSize);
    int *numsXOR = (int*)malloc(sizeof(int) * (numsSize + 1));

    // nums    = [0, 1, 1, 3]
    // numsXOR = [0, 0, 1, 0, 3]
    // numsXOR[0] = nums[0]
    // numsXOR[1] = nums[0] ^ nums[1]
    // numsXOR[2] = nums[0] ^ nums[1] ^ nums[2]
    // numsXOR[3] = nums[0] ^ nums[1] ^ nums[2] ^ nums[3]
    // I use extra 4 bytes at the beginning to avoid the check for ii == 0
    numsXOR[0] = 0;
    for (int ii = 0; ii < numsSize; ii++) {
        numsXOR[ii + 1] = nums[ii] ^ numsXOR[ii];
    }

    for (int ii = numsSize; ii > 0; ii--) {
        ret[numsSize - ii] = ~numsXOR[ii] & ((1ull << maximumBit) - 1);
    }

    *returnSize = numsSize;

    free(numsXOR);

    return ret;
}


// solution 3: no extra XOR array
int* getMaximumXor (int* nums, int numsSize, int maximumBit, int* returnSize)
{
    int *ret = (int*)malloc(sizeof(int) * numsSize);
    int xor = 0;

    // nums    = [0, 1, 1, 3]
    // numsXOR = [0, 0, 1, 0, 3]
    // numsXOR[0] = nums[0]
    // numsXOR[1] = nums[0] ^ nums[1]
    // numsXOR[2] = nums[0] ^ nums[1] ^ nums[2]
    // numsXOR[3] = nums[0] ^ nums[1] ^ nums[2] ^ nums[3]
    // I use extra 4 bytes at the beginning to avoid the check for ii == 0

    for (int ii = 0; ii < numsSize; ii++) {
        xor ^= nums[ii];
    }

    xor ^= (1ull << maximumBit) - 1;
    ret[0] = xor;

    for (int ii = 1; ii < numsSize; ii++) {
        xor ^= nums[numsSize - ii];
        ret[ii] = xor;
    }

    *returnSize = numsSize;

    return ret;
}
