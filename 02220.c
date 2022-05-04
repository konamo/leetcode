int countBits (int n)
{
    int count = 0;

    while (n) {
        n &= n - 1;
        count++;
    }
    return count;
}

int minBitFlips(int start, int goal)
{
    int xor = start ^ goal;


    return countBits(xor);
}
