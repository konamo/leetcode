int minFlips(int a, int b, int c)
{
    int result = (a | b) ^ c;
    int count = 0;

    for (int ii = 0; ii < 32; ii++) {
        if ((1ull << ii) & result) {
            if ((1ull << ii) & c) {
                count++;
            } else {
                if ((1ull << ii) & a) {
                    count++;
                }
                if ((1ull << ii) & b) {
                    count++;
                }
            }
        }
    }

    return count;
}
