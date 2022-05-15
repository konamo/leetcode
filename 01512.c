// solution 1
// time: O(n * n)
int numIdenticalPairs (int* nums, int numsSize)
{
    int count = 0;


    for (int ii = 0; ii < numsSize - 1; ii++) {
        for (int jj = ii + 1; jj < numsSize; jj++) {
            if (nums[ii] == nums[jj]) {
                count++;
            }
        }
    }

    return count;
}


void display(int *countMap, int size)
{
    for (int ii = 0; ii < size; ii++) {
        printf("%d ", countMap[ii]);
    }
    printf("\n");
    return;
}


// solution 2
// time: O(n)
// space: O(max)
int numIdenticalPairs (int* nums, int numsSize)
{
    int countMap[101];
    int count = 0;


    memset(countMap, 0, sizeof(countMap));
    for (int ii = 0; ii < numsSize; ii++) {
        countMap[nums[ii]]++;
    }

    for (int ii = 0; ii < 101; ii++) {
        if (countMap[ii]) {
            count += countMap[ii] * (countMap[ii] - 1) / 2;
        }
    }

    return count;
}


// solution 3
// time: O(n)
int numIdenticalPairs (int* nums, int numsSize)
{
    int countMap[101];
    int count = 0;


    memset(countMap, 0, sizeof(countMap));
    for (int ii = 0; ii < numsSize; ii++) {
        count += countMap[nums[ii]]++;
    }

    return count;
}
