#define MAX(a, b) (((a) > (b)) ? (a) : (b))



int expand(char *s, int left, int right)
{
    int L = left;
    int R = right;

    while (L >= 0 && R < strlen(s) && s[L] == s[R]) {
        L--;
        R++;
    }

    return R - L - 1;
}

char * longestPalindrome(char * s)
{
    if (s == NULL || strlen(s) == 1)
        return s;

    int start = 0;
    int end = 0;

    for (int ii = 0; ii < strlen(s); ii++) {
        int len1 = expand(s, ii, ii);   //assume odd length, try to extend Palindrome as possible
        int len2 = expand(s, ii, ii + 1); //assume even length.
        int len = MAX(len1, len2);

        if (len > end - start) {
            start = ii - (len - 1) / 2;
            end = ii + len / 2;
        }
    }

    s[end+1] = 0;
    return &s[start];
}
