int mycompare (const void *a, const void *b)
{
    const int *x = a;
    const int *y = b;

    return *x - *y;
}

int** fourSum (int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes)
{
    qsort(nums, numsSize, sizeof(int), mycompare);

    *returnSize = 0;
    int limit = 10;
    int **ret = (int**)malloc(sizeof(int*) * limit);

    for (int ii = 0; ii < numsSize - 3; ii++) {
        for (int jj = ii + 1; jj < numsSize - 2; jj++) {
            int left = jj + 1;
            int right = numsSize - 1;

            while (left < right) {
                int sum = nums[ii] + nums[jj] + nums[left] + nums[right];
                if (target == sum) {
                    if (*returnSize >= limit) {
                        limit += 10;
                        ret = (int**)realloc(ret, sizeof(int*) * limit);
                    }

                    ret[*returnSize] = (int*)malloc(sizeof(int) * 4);
                    ret[*returnSize][0] = nums[ii];
                    ret[*returnSize][1] = nums[jj];
                    ret[*returnSize][2] = nums[left];
                    ret[*returnSize][3] = nums[right];
                    (*returnSize)++;
                    left++;
                    right--;

                } else if (target < sum) {
                    right--;
                } else {
                    left++;
                }
            }
        }
    }


    if (*returnSize) {
        *returnColumnSizes = (int*)malloc(sizeof(int) * *returnSize);
        for (int ii = 0; ii < *returnSize; ii++) {
            (*returnColumnSizes)[ii] = 4;
        }
    }

    return ret;
}
