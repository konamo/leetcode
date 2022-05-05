int subsetXORSum (int* nums, int numsSize)
{
    int res = 0;
    int total;

    for (int ii = 0; ii < (1ull << numsSize); ii++) {
        total = 0;
        for (int jj = 0; jj < numsSize; jj++) {
            if (ii & (1ull << jj)) {
                total ^= nums[jj];
            }
        }
        res += total;
    }
    return res;
}
