#include <stdio.h>

int bitwiseComplement (int n)
{
    int leftmost;

    for (int ii = 0; ii < 32; ii++) {
        if (n & (1ull << ii)) {
            leftmost = ii;
        }
    }
    printf("%d\n", leftmost);

    return ~n & ((1ull << (leftmost+1)) - 1);
}

int bitwiseComplement (int n) {
    int x = 1;

    while (n > x)
        x = (x << 1) + 1;
    return x - n;
}

int bitwiseComplement(int n) {
    int x = 1;
    while (n > x)
        x = (x << 1) + 1;
    return n ^ x;
}

int main()
{
    bitwiseComplement(5);
    return 0;
}
