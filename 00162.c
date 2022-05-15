// only compare with the right neighbor
int findPeakElement (int* nums, int numsSize)
{
    for (int ii = 0; ii < numsSize - 1; ii++) {
        if (nums[ii] > nums[ii + 1]) {
            return ii;
        }
    }

    return numsSize - 1;
}

// solution 2:
int search(int* nums, int l, int r)
{
    if (l == r)
        return l;

    int mid = (l + r) / 2;
    if (nums[mid] > nums[mid + 1])
        return search(nums, l, mid);
    return search(nums, mid + 1, r);
}

int findPeakElement (int* nums, int numsSize)
{
    return search(nums, 0, numsSize - 1);
}


// solution 3:
int findPeakElement (int* nums, int numsSize)
{
    int left = 0;
    int right = numsSize - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] > nums[mid + 1]) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
