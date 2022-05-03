#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int binaryGap(int n)
{
    int dis = 0;
    int step = 0;
    int start = 0;

    while (n) {
        if (n & 0x1) {
            if (start) {
                dis = MAX(dis, step);
                step = 0;
            }
            start = 1;
        } else {
            if (start) {
                step++;
            }
        }
        n >>= 1;
    }

    return dis;
}


int binaryGap(int n)
{
    int dis = 0;
    int last = -1;

    for (int ii = 0; ii < 32; ii++) {
        if ((n >> ii) & 0x1) {
            if (last >= 0) {
                dis = MAX(dis, ii - last);
            }
            last = ii;
        }
    }
    return dis;
}
