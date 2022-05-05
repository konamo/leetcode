/**
 * Note: The returned array must be malloced, assume caller calls free().
 */


int countBits (int n)
{
    int count = 0;

    while (n) {
        n &= n - 1;
        count++;
    }
    return count;
}

int* sortByBits(int* arr, int arrSize, int* returnSize)
{
    int *bits = (int*)malloc(arrSize * sizeof(int));
    int *array = (int*)malloc(arrSize * sizeof(int));
    int index = 0;
    int start;

    *returnSize = arrSize;

    for (int ii = 0; ii < arrSize; ii++) {
        bits[ii] = countBits(arr[ii]);
    }

    for (int ii = 0; ii < 32; ii++) {
        start = index;
        for (int jj = 0; jj < arrSize; jj++) {
            if (bits[jj] == ii) {
                // add it and put it in the right order
                int kk;
                for (kk = start; kk < index; kk++) {
                    if (array[kk] > arr[jj]) {
                        for (int mm = index; mm > kk; mm--) {
                            array[mm] = array[mm-1];
                        }
                        break;
                    }
                }
                array[kk] = arr[jj];
                index++;
            }
        }
    }


    return array;
}


int mycompare (const void *a, const void *b)
{
    const int *x = a;
    const int *y = b;

    if (countBits(*x) == countBits(*y)) {
        return *x - *y;
    } else {
        return countBits(*x) - countBits(*y);
    }
}

int* sortByBits(int* arr, int arrSize, int* returnSize)
{
    int *array = (int*)malloc(arrSize * sizeof(int));

    memcpy(array, arr, sizeof(int) * arrSize);
    qsort(array, arrSize, sizeof(int), mycompare);

    *returnSize = arrSize;

    return array;
}
