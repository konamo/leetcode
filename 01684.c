int countConsistentStrings (char * allowed, char ** words, int wordsSize)
{
    int dict[26] = {0};
    int count = 0;



    for (int ii = 0; ii < strlen(allowed); ii++) {
        dict[allowed[ii] - 'a']++;
    }


    for (int ii = 0; ii < wordsSize; ii++) {
        int jj;
        for (jj = 0; jj < strlen(words[ii]); jj++) {
            if (dict[words[ii][jj] - 'a'] == 0) {
                break;
            }
        }
        if (jj == strlen(words[ii])) {
            count++;
        }
    }


    return count;
}


int countConsistentStrings (char * allowed, char ** words, int wordsSize)
{
    int bitmap = 0;
    int count = wordsSize;

    for (int ii = 0; ii < strlen(allowed); ii++) {
        bitmap |= 1ull << (allowed[ii] - 'a');
    }

    for (int ii = 0; ii < wordsSize; ii++) {
        for (int jj = 0; jj < strlen(words[ii]); jj++) {
            if ((bitmap & (1ull << (words[ii][jj] - 'a'))) == 0) {
                count--;
                break;
            }
        }
    }

    return count;
}
