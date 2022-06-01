#define MAX(a, b) ((a) > (b) ? (a) : (b))


int countZero (int *nums, int start, int end)
{
    int count = 0;


    for (int ii = start; ii <= end; ii++) {
        if (nums[ii] == 0) {
            count++;
        }
    }

    return count;
}

// solution 1: brute force
int longestOnes (int* nums, int numsSize, int k)
{
    int maxLen = 0;

    for (int ii = 0; ii < numsSize; ii++) {
        for (int jj = ii; jj < numsSize; jj++) {
            if (countZero(nums, ii, jj) <= k) {
                maxLen = MAX(maxLen, jj - ii + 1);
            }
        }
    }

    return maxLen;
}


// solution 2: pre-calculate the number of zeroes
int longestOnes (int* nums, int numsSize, int k)
{
    int maxLen = 0;
    int start = 0;
    int end = 0;
    int count = 0;
    int zeroes[numsSize];
    int current;

    memset(zeroes, 0, sizeof(zeroes));

    for (int ii = 0; ii < numsSize; ii++) {
        if (nums[ii] == 0) {
            count++;
        }
        zeroes[ii] = count;
    }


    while (end < numsSize) {
        if (nums[start] == 0) {
            current = 1;
        } else {
            current = 0;
        }

        if (zeroes[end] - zeroes[start] + current <= k) {
            maxLen = MAX(maxLen, end - start + 1);
        } else {
            start++;
        }
        end++;
    }

    return maxLen;
}

// solution 3
// Find the longest subarray with at most k zeros.
int longestOnes (int* nums, int numsSize, int k)
{
    int start = 0, end;

    for (end = 0; end < numsSize; end++) {
        if (nums[end] == 0)
            k--;

        if (k < 0 && nums[start++] == 0)
            k++;
    }

    return end - start;
}
