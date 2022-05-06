#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

// to check if the string[ii, jj] inclusive is NICE
bool isNice (const char *s, int ii, int jj)
{
    int lower[26] = {0};
    int upper[26] = {0};

    while (ii <= jj) {
        if (s[ii] <= 'Z' && s[ii] >= 'A') {
            lower[s[ii] - 'A']++;
        } else {
            upper[s[ii] - 'a']++;
        }
        ii++;
    }

    for (int ii = 0; ii < 26; ii++) {
        if (lower[ii] && upper[ii]) {
            NULL;
        } else if (lower[ii] == 0 && upper[ii] == 0) {
            NULL;
        } else {
            return false;
        }
    }

    return true;
}

// brute force solution
int longestNiceSubstring2 (const char * s)
{
    const int len = strlen(s);
    int max = 0;


    for (int ii = 0; ii < len - 1; ii++) {
        for (int jj = ii + 1; jj < len; jj++) {
            if (isNice(s, ii, jj)) {
                max = MAX(max, jj - ii + 1);
            }
        }
    }

    return max;
}

// to check if the current char (c) only has lower case letter or
// upper case letter in string[ii, jj] inclusive
bool isNiceC (const char *s, const char c, const int ii, const int jj)
{
    int lower[26] = {0};
    int upper[26] = {0};

    for (int kk = ii; kk <= jj; kk++) {
        if (s[kk] <= 'Z' && s[kk] >= 'A') {
            upper[s[kk] - 'A']++;
        } else {
            lower[s[kk] - 'a']++;
        }
    }

    // 'a' = 0x61 = 0b 0110 0001
    // 'A' = 0x41 = 0b 0100 0001
    // c & 0b1101 1111
    if (upper[(c & 0xdf) - 'A'] && lower[(c & 0xdf) - 'A']) {
        return true;
    }

    return false;
}

int longestNiceSubstringHelper(char * s, int ii, int jj)
{
    int a = 0;
    int b = 0;


    if (jj - ii < 1) {
        return 0;
    }

    for (int kk = ii; kk <= jj; kk++) {
        if (!isNiceC(s, s[kk], ii, jj)) {
            // kick out kk
            a = longestNiceSubstringHelper(s, ii, kk - 1);
            b = longestNiceSubstringHelper(s, kk + 1, jj);
            return MAX(a, b);
        }
    }

    // no breaking char
    return jj - ii + 1;
}

char* longestNiceSubstring (char *s)
{
    int len = strlen(s);
    int max = longestNiceSubstringHelper(s, 0, len - 1);

    printf("max %d\n", max);

    if (max > 0) {
        for (int ii = 0; ii < len - max + 1; ii++) {
            if (isNice(s, ii, ii + max - 1)) {
                s[ii + max] = 0;
                return &s[ii];
            }
        }
    }
    return "";
}

int main ()
{
    char test_str[100];

    strncpy(test_str, "YazaAay", sizeof(test_str));
    printf("%s\n", longestNiceSubstring(test_str));


    strncpy(test_str, "Bb", sizeof(test_str));
    printf("%s\n", longestNiceSubstring(test_str));

    strncpy(test_str, "c", sizeof(test_str));
    printf("%s\n", longestNiceSubstring(test_str));

    strncpy(test_str, "xLeElzxgHzcWslEdgMGwEOZCXwwDMwcEhgJHLL", sizeof(test_str));
    printf("%s\n", longestNiceSubstring(test_str));


    return 0;
}
