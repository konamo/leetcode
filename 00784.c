#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void displayMem (const uint8_t *data, const int size)
{
    for (int ii = 0; ii < size; ii++) {
        printf("%02x ", data[ii]);
    }

    printf("\n");
    return;
}


char ** letterCasePermutation(char * s, int* returnSize)
{
    int index = 0;
    int len = strlen(s);
    int count = 0;
    char temp[len + 1];
    int pos;

    for (int ii = 0; ii < len; ii++) {
        if (s[ii] <= 'z' && s[ii] >= 'a') {
            count++;
        } else if (s[ii] <= 'Z' && s[ii] >= 'A') {
            s[ii] += 'a' - 'A';
            count++;
        }
    }

    char **ret = (char**)malloc((1ull << count) * sizeof(char*));
    if (ret == NULL) {
        return NULL;
    }

    *returnSize = 1ull << count;

    for (int ii = 0; ii < (1ull << count); ii++) {
        strcpy(temp, s);
        pos = 0;
        for (int jj = 0; jj < len; jj++) {
            if ((temp[jj] >= 'a') && (temp[jj] <= 'z')) {
                if (ii & (1ull << pos)) {
                    temp[jj] += 'A' - 'a';
                }
                pos++;
            }
        }

        ret[index] = (char*)malloc(len + 1);
        strcpy(ret[index], temp);
        index++;
    }

    return ret;
}

int main ()
{
    int ret;
    char **str;
    char s[] = "a1C2";

    str = letterCasePermutation(s, &ret);

    printf("Total %d strings:\n", ret);
    for (int ii = 0; ii < ret; ii++) {
        printf("%d: %s\n", ii, str[ii]);
        free(str[ii]);
    }
    free(str);

    return 0;
}
