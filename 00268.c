int missingNumber(int* nums, int numsSize)
{
    int target = numsSize;

    for (int ii = 0; ii < numsSize; ii++) {
        target += ii - nums[ii];
    }

    return target;
}


int missingNumber(int* nums, int numsSize)
{
    unsigned long long expected, tota, n;
    int i;

	n = numsSize;
    total = 0;
    for (i = 0; i < numsSize; i++)
        total += (unsigned long long) nums[i];

    expected = (n * (n + 1)) / 2;
    return expected - total;
}


int missingNumber(int* nums, int numsSize)
{
    //we want to Xor all numbers from 0 to n twice so should be zero
    //because num^num = 0
    //but number that is missing will appear only once in Xor, and that's what will be left..
    int missing_number = numsSize;
    for(int i =0; i < numsSize; i++)
        missing_number ^= nums[i] ^ i;
    return missing_number;
}
