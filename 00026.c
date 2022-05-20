void swap (int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
    return;
}

int removeDuplicates(int* nums, int numsSize)
{
    int ii = 0;
    int jj = ii + 1;


    while (jj < numsSize) {
        if (nums[ii] == nums[jj]) {
            jj++;
        } else {
            ii++;
            swap(&nums[ii], &nums[jj]);
            jj++;
        }
    }


    return ii + 1;
}
