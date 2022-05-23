#define MAX(a, b) ((a) > (b) ? (a) : (b))

int findBadGuy (char *s, int k, int left, int right)
{
    int countMap['z' + 1];

    if (right - left < k) {
        return 0;
    }

    memset(countMap, 0, sizeof(countMap));
    for (int ii = left; ii < right; ii++) {
        countMap[s[ii]]++;
    }

    // find the bad guy
    for (int ii = left; ii < right; ii++) {
        if (countMap[s[ii]] >= k) {
            continue;
        }

        int midNext = ii + 1;
        while (midNext < right && countMap[s[midNext]] < k) {
            midNext++;
        }
        return MAX(findBadGuy(s, k, left, ii), findBadGuy(s, k, midNext, right));
    }

    return right - left;
}



int longestSubstring(char * s, int k)
{
    return findBadGuy(s, k, 0, strlen(s));
}
