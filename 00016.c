// solution 1: brute force
int threeSumClosest(int* nums, int numsSize, int target)
{
    int min = INT32_MAX;
    int ret;


    for (int ii = 0; ii < numsSize - 2; ii++) {
        for (int jj = ii + 1; jj < numsSize - 1; jj++) {
            for (int kk = jj + 1; kk < numsSize; kk++) {
                if (abs(nums[ii] + nums[jj] + nums[kk] - target) < min) {
                    min = abs(nums[ii] + nums[jj] + nums[kk] - target);
                    ret = nums[ii] + nums[jj] + nums[kk];
                }
            }
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

int threeSumClosest(int* nums, int numsSize, int target)
{
    if (numsSize < 3)
        return -1;

    int ret = nums[0] + nums[1] + nums[2];

    qsort(nums, numsSize, sizeof(int), mycompare);

    for (int ii = 0; ii < numsSize - 2; ii++) {
        //2sum
        int left = ii + 1;
        int right = numsSize - 1;

        while (left < right) {
            int sum = nums[ii] + nums[left] + nums[right];

            if (sum > target) {
                right--;
            } else {
                left++;
            }

            if (abs(sum - target) < abs(ret - target)) {
                ret = sum;
            }
        }
    }


    return ret;
}
