/*Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
*/


void swap (int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
    return;
}

// this solution doesn't work because it changes the
// relative ordeer of the non-zero elements
// two points meet each other in the half way
void moveZeroes(int* nums, int numsSize)
{
    int ii = 0;
    int jj = numsSize - 1;



    while (ii < jj) {
        if (nums[ii] == 0) {
            swap(&nums[ii], &nums[jj]);
            jj--;
        } else {
            ii++;
        }
    }


    return;
}


// solution 2: two points move towards same direction
void moveZeroes(int* nums, int numsSize)
{
    int ii = 0;
    int jj;


    // find the first position of zero element
    while (ii < numsSize) {
        if (nums[ii]) {
            ii++;
        } else {
            break;
        }
    }

    jj = ii + 1;

    while (jj < numsSize) {
        if (nums[jj]) {
            // swap jj with ii if jj is non-zero
            // ii is pointing to zero element
            swap(&nums[ii], &nums[jj]);
            ii++;
            jj++;
        } else {
            jj++;
        }
    }


    return;
}
