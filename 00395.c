#define MAX(a, b) ((a) > (b) ? (a) : (b))

// solution 1
// find unqualified char in [left, right), right is exclusive
int findBadGuy (char *s, int k, int left, int right)
{
    // extra space for quick access
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

        // this is an optimization to make it faster
        int midNext = ii + 1;
        while (midNext < right && countMap[s[midNext]] < k) {
            midNext++;
        }

        return MAX(findBadGuy(s, k, left, ii), findBadGuy(s, k, midNext, right));
    }

    return right - left;
}

int longestSubstring (char * s, int k)
{
    return findBadGuy(s, k, 0, strlen(s));
}





// solution 2
int getMaxUniqueLetters (const char *s)
{
    bool map[26] = {0};
    int maxUnique = 0;

    for (int ii = 0; ii < strlen(s); ii++) {
        if (!map[s[ii] - 'a']) {
            maxUnique++;
            map[s[ii] - 'a'] = true;
        }
    }

    return maxUnique;
}

// implement this algorithm is not that hard
// the hardest part is why it works? how to prove it?
int longestSubstring (const char * s, int k)
{
    int countMap[26];
    int maxUnique = getMaxUniqueLetters(s);
    int result = 0;

    for (int currUnique = 1; currUnique <= maxUnique; currUnique++) {
        // reset countMap
        memset(countMap, 0, sizeof(countMap));
        int windowStart = 0, windowEnd = 0, idx = 0, unique = 0, countAtLeastK = 0;
        while (windowEnd < strlen(s)) {
            // expand the sliding window
            if (unique <= currUnique) {
                idx = s[windowEnd] - 'a';
                if (countMap[idx] == 0) unique++;
                countMap[idx]++;
                if (countMap[idx] == k) countAtLeastK++;
                windowEnd++;
            }
            // shrink the sliding window
            else {
                idx = s[windowStart] - 'a';
                if (countMap[idx] == k) countAtLeastK--;
                countMap[idx]--;
                if (countMap[idx] == 0) unique--;
                windowStart++;
            }

            if (unique == currUnique && unique == countAtLeastK)
                result = MAX(windowEnd - windowStart, result);
        }
    }

    return result;
}
