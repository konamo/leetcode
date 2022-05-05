int xorOperation(int n, int start)
{
    int xor = 0;


    for (int ii = start; ii < start + 2 * n; ii += 2) {
        xor ^= ii;
    }

    return xor;
}
