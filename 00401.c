/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

const uint8_t lookupHours [][] =
{
    {"0"},
    {"1", "2", "4", "8",},
    {"3", "5", "6", "9", "10",},
    {"7", "11"},
};

const uint8_t lookupMinutes [][] =
{
    {"00"},
    {"01", "02", "04", "08", "16", "32",},
    {"03", "05", "09", "17", "33", "06", "10", "18", "34", "12", "20", "36", "24", "40", "48"},
    {},
};

char ** readBinaryWatch(int turnedOn, int* returnSize)
{

    for (ii = 0; ii < turnedOn; ii++) {
        for (jj = 0; jj < ; jj++) {
            lookupHours[ii];
            for (kk = 0; kk < ; kk++) {
                lookupMinutes[turnedOn - ii];
            }
        }
    }

    return;
}



int countBits (int n)
{
    int count = 0;

    while (n) {
        n &= n - 1;
        count++;
    }

    return count;
}

char ** readBinaryWatch(int turnedOn, int* returnSize)
{
    char** ret = (char**)malloc(sizeof(char*) * 12 * 60);
    int index = 0;

    for (int hours = 0; hours < 12; hours++) {
        for (int minutes = 0; minutes < 60; minutes++) {
            if (countBits(hours << 6 | minutes) == turnedOn) {
                char *str = (char*)malloc(6);
                int ii;

                ii = sprintf(&str[0], "%d:", hours);
                sprintf(&str[ii],"%02d", minutes);

                ret[index++] = str;
            }
        }
    }

    *returnSize = index;
    return ret;
}
