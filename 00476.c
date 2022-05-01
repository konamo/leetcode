

int findComplement(int num)
{
    int n = num;
    int ii = 0, shift;

    while (num) {
        if (num & 0x1) {
            shift = ii;
        }
        ii++;
        num >>= 1;
    }

    return (1ull << (shift + 1)) - 1 - n;
}


/*
 * num          = 00000101
 * mask         = 11111000
 * ~mask & ~num = 00000010
 *
 */
int findComplement(int num) {
    uint32_t mask = -1;

    while (num & mask)
        mask <<= 1;
    return ~mask & ~num;
}

/*
I basically check every bit of number by XOR'ing it with appropriate power of 2 which leads to its invertion.
For example:

Entered: 4=>100;
100 ^ 001 = 101;
101 ^ 010 = 111;
111 ^ 100 = 011;
Out:     011=>3;

 */
int findComplement(int num) {
    uint32_t i;

    for(i=1; i<=num; i*=2)
        num^=i;
    return num;
}
