int numberOfSteps (int num)
{
    int step = 0;

    while (num) {
        if (num % 2) {
            num--;
        } else {
            num /= 2;
        }
        step++;
    }

    return step;
}

int numberOfSteps (int num)
{
    int step = 0;

    while (num) {
        if (num & 0x1) {
            num &= ~(1ull);
        } else {
            num >>= 1;
        }
        step++;
    }
    return step;
}


/*
 * For the binary representation from right to left(until we find the leftmost 1):
if we meet 0, result += 1 because we are doing divide;
if we meet 1, result += 2 because we first do "-1" then do a divide;
ony exception is the leftmost 1, we just do a "-1" and it becomse 0 already.
 */
int numberOfSteps (int num)
{
	if(!num)
        return 0;
    int res = 0;

    while (num) {
        res += (num & 1) ? 2 : 1;
        num >>= 1;
    }
    return res - 1;
}
