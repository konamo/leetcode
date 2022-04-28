


// sort + binary search
int singleNumber(int* nums, int numsSize){

}




// XOR
int singleNumber(int* nums, int numsSize)
{
    int ii;
    int x = 0;

    for (ii = 0; ii < numsSize; ii++) {
        x ^= nums[ii];
    }

    return x;
}
