#include <stdio.h>
#include <stdint.h>
#include <math.h>

uint32_t reverseBits (uint32_t n) {
    int start = 0;
    int end = 31;
    int t;

    while (start < end) {
        t = n & (0x1 << start);
        n = (n & ~(0x1 << start)) | (n & (0x1 << end));
        n = (n & ~(0x1 << end)) | (t << end);
        start++;
        end--;
    }
    return n;
}


uint32_t reverseBits2 (uint32_t n)
{
    uint32_t m = 0;
    for (int i = 0; i < 32; i++, n >>= 1) {
        m <<= 1;
        m |= n & 1;
    }
    return m;
}

uint32_t reverseBits3 (uint32_t n)
{
    n = (n >> 16) | (n << 16);
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
    return n;
}

int main ()
{
    printf("x%x\n", reverseBits(0xabcdefa5));
    printf("x%x\n", reverseBits2(0xabcdefa5));
    printf("x%x\n", reverseBits3(0xabcdefa5));

    printf("%f\n", sqrt(-4));
    return 0;
}
