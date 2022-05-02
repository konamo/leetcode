#include <stdio.h>
#include <stdbool.h>

bool hasAlternatingBits (int n)
{
    for (int ii = 0; ii < 31; ii++) {
        if (((n & 0x3) == 0b01) || ((n & 0x3) == 0b10)) {
            NULL;
        } else {
            return false;
        }
        n >>= 1;

        if (n == 0) {
            return true;
        }
    }

    return true;
}

bool hasAlternatingBits (int n)
{
    int num = n;
    int ii= 0;
    int shift;


    while (n) {
        if (n & 0x1) {
            shift = ii;
        }
        ii++;
        n >>= 1;
    }

    n = num;
    if ((n ^ (n >> 1)) == ((1ull << (shift + 1)) - 1)) {
        return true;
    }
    return false;
}

bool hasAlternatingBits (int n)
{
    n ^= (n >> 1);
    return (n & (n+1)) == 0;
}

bool hasAlternatingBits (int n)
{
    // n & (n >> 1) == 0, no consecutive 1s
    // the 2nd part is hard to understand??
    return (n & (n >> 1)) == 0 && (n & (n >> 2)) == (n >> 2);
}

int main()
{
    printf("%d\n", hasAlternatingBits(5));
    printf("%d\n", hasAlternatingBits(7));
    printf("%d\n", hasAlternatingBits(4));
    printf("%d\n", hasAlternatingBits(11));
    return 0;
}
