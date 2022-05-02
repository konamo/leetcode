
int countBits (int n)
{
    int count = 0;

    while (n) {
        n &= n - 1;
        count++;
    }
    return count;
}

int countPrimeSetBits(int left, int right)
{
    int count = 0;
    int bits;

    for (int ii = left; ii <= right; ii++) {
        bits = countBits(ii);
        if (bits == 2 || bits == 3 || bits == 5 || bits == 7 ||
                bits == 11 || bits == 13 || bits == 17 || bits == 19) {
            count++;
        }
    }

    return count;
}

const uint8_t lookup[] =
{
    0, 0, 1, 1, 0,
    1, 0, 1, 0, 0,
    0, 1, 0, 1, 0,
    0, 0, 1, 0, 1,
};

int countPrimeSetBits(int left, int right)
{
    int count = 0;

    while (left <= right) {
        count += lookup[countBits(left++)];
    }
    return count;
}

#define BITMAP (0b10100010100010101100)

int countPrimeSetBits(int left, int right)
{
    int count = 0;

    while (left <= right) {
        count += (BITMAP >> countBits(left++)) & 0x1;
    }
    return count;
}
