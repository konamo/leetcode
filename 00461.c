int countBits (int n)
{
    int count = 0;


    while (n) {
        n &= n - 1;
        count++;
    }
    return count;
}

int hammingDistance(int x, int y)
{
    return countBits(x ^ y);
}
