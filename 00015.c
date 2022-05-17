// solution 1: brute force, needs to remove duplicates
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{
    int **ret = NULL;
    *returnSize = 0;

    for (int ii = 0; ii < numsSize - 2; ii++) {
        for (int jj = ii + 1; jj < numsSize - 1; jj++) {
            for (int kk = jj + 1; kk < numsSize; kk++) {
                if (nums[ii] + nums[jj] + nums[kk] == 0) {
                    (*returnSize)++;
                    if (ret == NULL) {
                        ret = (int**)malloc(sizeof(int*) * 1);
                    } else {
                        ret = (int**)realloc(ret, sizeof(int*) * *returnSize);
                    }
                    ret[*returnSize - 1] = (int*)malloc(sizeof(int) * 3);
                    ret[*returnSize - 1][0] = nums[ii];
                    ret[*returnSize - 1][1] = nums[jj];
                    ret[*returnSize - 1][2] = nums[kk];
                }
            }
        }
    }

    if (*returnSize) {
        *returnColumnSizes = (int*)malloc(*returnSize * sizeof(int));
        for (int ii = 0; ii < *returnSize; ii++) {
            (*returnColumnSizes)[ii] = 3;
        }
    }


    return ret;
}

// solution 2: sort and then 2sum sweep
void display(int *nums, int numsSize)
{
    for (int ii = 0; ii < numsSize; ii++) {
        printf("%02d ", nums[ii]);
    }
    printf("\n");
    return;
}


int mycompare (const void *a, const void *b)
{
    const int *x = a;
    const int *y = b;

    return *x - *y;
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{
    int **ret = NULL;
    *returnSize = 0;
    int limit = numsSize;

    qsort(nums, numsSize, sizeof(int), mycompare);

    int ii = 0;
    while (ii < numsSize - 2) {
        //2sum
        int left = ii + 1;
        int right = numsSize - 1;

        while (left < right) {
            if (nums[left] + nums[right] == -nums[ii]) {
                if (ret == NULL) {
                    ret = (int**)malloc(sizeof(int*) * limit);
                } else if (*returnSize >= limit) {
                    limit += numsSize;
                    ret = (int**)realloc(ret, sizeof(int*) * limit);
                }
                ret[*returnSize] = (int*)malloc(sizeof(int) * 3);
                ret[*returnSize][0] = nums[ii];
                ret[*returnSize][1] = nums[left];
                ret[*returnSize][2] = nums[right];
                (*returnSize)++;

                while (left < right && nums[left] == nums[left + 1])
                    left++;
                left++;
                while (left < right && nums[right] == nums[right - 1])
                    right--;
                right--;
            } else if (nums[left] + nums[right] < -nums[ii]) {
                left++;
            } else {
                right--;
            }
        }

        // avoid duplicates
        while (ii < (numsSize - 2) && nums[ii] == nums[ii+1]) {
            ii++;
        }
        ii++;
    }


    if (*returnSize) {
        *returnColumnSizes = (int*)malloc(*returnSize * sizeof(int));
        for (int ii = 0; ii < *returnSize; ii++) {
            (*returnColumnSizes)[ii] = 3;
        }
    }

    return ret;
}
