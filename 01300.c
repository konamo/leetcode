#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int sumArray(int *arr, int arrSize, int value)
{
    int sum = 0;

    for (int ii = 0; ii < arrSize; ii++) {
        if (arr[ii] > value) {
            sum += value;
        } else {
            sum += arr[ii];
        }
    }

    return sum;
}

int findBestValue(int* arr, int arrSize, int target)
{
    int delta = INT32_MAX;
    int ret;
    int min = arr[0];
    int max = arr[0];


    for (int ii = 1; ii < arrSize; ii++) {
        min = MIN(min, arr[ii]);
        max = MAX(max, arr[ii]);
    }

    int left = MIN(min, target / arrSize);
    int right = max;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        int s = sumArray(arr, arrSize, mid);
        if (target == s) {
            right = mid - 1;
        } else if (target > s) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }

        if (delta == abs(target - s)) {
            ret = MIN(ret, mid);
        } else if (delta > abs(target - s)) {
            ret = mid;
            delta = abs(target - s);
        }
    }

    return ret;
}



// solution 2
// sort ascending
int mycompare (const void *a, const void *b)
{
    const int *x = a;
    const int *y = b;

    return *x - *y;
}

// 3 cases:
// a. if target > array sum, return the max
// b. if target < array sum, return target / arrSize
// c. remove small elements and it's basically case b
int findBestValue(int* arr, int arrSize, int target)
{
    qsort(arr, arrSize, sizeof(int), mycompare);

    int ii = 0;
    while (ii < arrSize && target > arr[ii] * (arrSize - ii)) {
        target -= arr[ii++];
    }

    if (ii == arrSize) {
        return arr[arrSize - 1];
    } else {
        int ret = target / (arrSize - ii);
        if (abs(target - (arrSize - ii) * ret) <= abs(target - (arrSize - ii) * (ret + 1))) {
            return ret;
        } else {
            return ret + 1;
        }
    }
}
