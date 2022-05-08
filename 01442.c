// solution 1: search for XOR == 0
int countTriplets (int* arr, int arrSize)
{
    int xor;
    int count = 0;


    for (int ii = 0; ii < arrSize - 1; ii++) {
        xor = arr[ii];
        for (int jj = ii + 1; jj < arrSize; jj++) {
            xor ^= arr[jj];
            if (xor == 0) {
                count += jj - ii;
            }
        }
    }

    return count;
}

// solution 2: prefix XOR
int countTriplets (int* arr, int arrSize)
{
    int prefixXOR[arrSize + 1];
    int count = 0;


    prefixXOR[0] = 0;
    for (int ii = 0; ii < arrSize; ii++) {
        prefixXOR[ii + 1] = prefixXOR[ii] ^ arr[ii];
    }

    for (int ii = 0; ii < arrSize; ii++) {
        for (int jj = ii + 1; jj < arrSize + 1; jj++) {
            if (prefixXOR[ii] == prefixXOR[jj]) {
                count += jj - ii - 1;
            }
        }
    }

    return count;
}



// solution 3: hashmap
// the idea is to use 2 hashmap
// one for the count instance
// the other one for the total index so far
//
// for example, 0, 2, 1, 0, 6, 7, 2..... 2
// for the first 2, count[2] = 1, total[2] = 1
// for the second 2, count[2] = 2, total[2] = 1 + 6 = 7
// if we have 3rd 2, count[2] = 3, total[2] = 1 + 6 + index
// for the 3rd 2, we need jj - 2nd 2's index + (jj - 1st 2's index)
// which means we use 3rd 2's index twice.
int countTriplets (int* arr, int arrSize)
{
    int prefixXOR[arrSize + 1];
    int res = 0;
    int count[100] = {0};
    int total[100] = {0};


    prefixXOR[0] = 0;
    for (int ii = 0; ii < arrSize; ii++) {
        prefixXOR[ii + 1] = prefixXOR[ii] ^ arr[ii];
    }

    for (int ii = 0; ii < arrSize + 1; ii++) {
        res += count[prefixXOR[ii]]++ * (ii - 1) - total[prefixXOR[ii]];
        total[prefixXOR[ii]] += ii;
    }
    return res;
}
