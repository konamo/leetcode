int countBits(int n)
{
    int count = 0;


    for (int ii = 0; ii < 32; ii++) {
        if (n & 0x1) {
            count++;
        }
        n >>= 1;
    }

    return count;
}


bool isPowerOfFour(int n)
{
    if (n <= 0) {
        return false;
    }

    int count = countBits(n);
    printf("%d\n", count);
    if (count == 1) {
        for (int ii = 0; ii < 32; ii++) {
            if (n & 0x1) {
                if (ii % 2) {
                    return false;
                } else {
                    return true;
                }
            }
            n >>= 1;
        }
    } else {
        return false;
    }

    return true;
}



// 1  0b0001
// 4  0b0100
// 16 0b1   0000
// 64 0b100 0000
const uint8_t lookup[16] =
{
    0, 1, 0, 0,
    1, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
};

const uint32_t lookup2[16] =
{
    1ull << 0, 1ull << 2, 1ull << 4, 1ull << 6,
    1ull << 8, 1ull << 10, 1ull << 12, 1ull << 14,
    1ull << 16, 1ull << 18, 1ull << 20, 1ull << 22,
    1ull << 24, 1ull << 26, 1ull << 28, 1ull << 30,
};

bool isPowerOfFour(int n)
{
    if (n <= 0) {
        return false;
    }

    while (n) {
        if ((n & 0xf) == 0) {
            NULL;
        } else if (!lookup[n & 0xf]) {
            return false;
        } else {
            if ((n & 0xfffffff0) == 0) {
                return true;
            } else {
                return false;
            }
        }
        n >>= 4;
    }

    return false;
}

const uint32_t lookup2[16] =
{
    1ull << 0, 1ull << 2, 1ull << 4, 1ull << 6,
    1ull << 8, 1ull << 10, 1ull << 12, 1ull << 14,
    1ull << 16, 1ull << 18, 1ull << 20, 1ull << 22,
    1ull << 24, 1ull << 26, 1ull << 28, 1ull << 30,
};
bool isPowerOfFour(int n)
{
    for (int ii; ii < 16; ii++) {
        if (lookup2[ii] == n) {
            return true;
        }
    }
    return false;
}


bool isPowerOfFour(int num)
{
    // check if there is only a single bit 1
    // (num & (num - 1)) == 0

	return num > 0 && (num & (num - 1)) == 0 && (num & 0xAAAAAAAA) == 0;
}

bool isPowerOfFour(int num)
{
    // check if there is only a single bit 1
    // (num & (num - 1)) == 0

	return num > 0 && (num & (num - 1)) == 0 && (num & 0x55555555);
}
