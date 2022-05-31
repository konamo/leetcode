#define MAX(a, b) ((a) > (b) ? (a) : (b))

int getMaxCount (const int count[])
{
    int maxCount = 0;


    for (int ii = 'A'; ii <= 'Z'; ii++) {
        maxCount = MAX(maxCount, count[ii]);
    }

    return maxCount;
}

int characterReplacement (const char * s, const int k)
{
    int count['Z' + 1] = {0};
    int maxCount;
    int maxLen = 0;
    int start = 0;
    int end = 0;


    while (end < strlen(s)) {
        count[s[end]]++;
        maxCount = getMaxCount(count);

        if (end - start + 1 > k + maxCount) {
            // decrease the counter on [start]
            count[s[start]]--;
            start++;
        } else {
            maxLen = MAX(maxLen, end - start + 1);
        }
        // here is the tricky point:
        // no matter if the condition is met or not, the end variable gets increased
        // because we don't want to shrink the window
        // Think about it in this way: we first expand the window as long as possible
        // and then we have no interest on any smaller window even if it meets the condition
        end++;
    }

    return maxLen;
}
