
// traditional
int hammingWeight(uint32_t n) {
    int count = 0;
    int ii;


    for (ii = 0; ii < 32; ii++) {
        if (ii & 0x1) {
            count++;
        }
        ii >>= 1;
    }
    return count;
}


// & trick
// n        n-1             & result
// 0b1101   0b1100          0b1100
// 0b1100   0b1011          0b1000
// 0b1000   0b0111          0b0000
int hammingWeight(uint32_t n) {
    int count = 0;

    while (n) {
        n &= n - 1;
        count++;
    }

    return count;
}








// lookup table
const uint8_t lookup_table [256] = {
    0, 1, 1, 2, 1, 2,
};

int hammingWeight(uint32_t n) {
    int count = 0;

    while (n) {
        count += lookup_table[n & 0xff];
        n >>= 8;
    }

    return count;
}
