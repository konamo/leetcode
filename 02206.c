bool divideArray (int* nums, int numsSize)
{
    int countMap[501] = {0};

    for (int ii = 0; ii < numsSize; ii++) {
        countMap[nums[ii]]++;
    }

    for (int ii = 0; ii < 501; ii++) {
        if (countMap[ii] % 2) {
            return false;
        }
    }
    return true;
}
