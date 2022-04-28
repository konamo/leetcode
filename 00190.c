#include <stdio.h>
#include <stdint.h>


// swap
// bit 31 -- bit 0
// bit 30 -- bit 1
// bit 29 -- bit 2
// ....
uint32_t reverseBits (uint32_t n) {
    int ii;
    uint32_t l, h;


    for (ii = 0; ii < 16; ii++) {
        // get the lower bit
        l = (n & (0x1ul << ii)) >> ii;

        // get the higher bit
        h = (n & (0x1ul << (31 - ii))) >> (31 - ii);

        // set lower bit to 0
        n &= ~(0x1ul << ii);

        // set high bit to 0
        n &= ~(0x1ul << (31 - ii));

        // swap
        n |= l << (31 - ii);
        n |= h << ii;
    }

    return n;
}

// get bits from n right to left
uint32_t reverseBits2 (uint32_t n)
{
    uint32_t m = 0;
    int ii;

    for (ii = 0; ii < 32; ii++) {
        m <<= 1;
        m |= n & 1;
        n >>= 1;
    }

    return m;
}


// ABCDE....XYZ
// 1st swap: ...XYZ | ABCDE...
// 2nd swap: XYZ|...| ...|ABCD
// .....            | ...|CD|AB
// last             | ...|D|C|B|A
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

    return 0;
}
