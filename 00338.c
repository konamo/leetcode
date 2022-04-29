int count(uint32_t n)
{
    int ii = 0;

    while (n) {
        n &= n - 1;
        ii++;
    }
    return ii;
}

int* countBits(int n, int* returnSize)
{
    int *array = (int*)malloc(sizeof(int) * (n+1));
    int ii;


    for (ii = 0; ii <= n; ii++) {
        array[ii] = count(ii);
    }

    *returnSize = n + 1;
    return array;
}



int* countBits(int n, int* returnSize)
{
    int *array = (int*)malloc(sizeof(int) * (n+1));

    array[0] = 0;

    // we can compute current set bit count using previous count
    // as x/2 in O(1) time
    // i%2 will be 0 for even number ans 1 for odd number
    for(int i = 1; i<=n; ++i)
        array[i] = array[i/2] + i%2;
    *returnSize = n + 1;
    return array;
}
