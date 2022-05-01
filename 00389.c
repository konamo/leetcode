char findTheDifference (char * s, char * t)
{
    uint8_t xor = 0;

    while (*s && *t) {
        xor ^= *s ^ *t;
        s++;
        t++;
    }

    xor ^= *t;

    return xor;
}



char findTheDifference (char * s, char * t)
{
    int sum = 0;

    while (*t && *s) {
        sum = (sum + *t++ - *s++) % 256;
    }

    sum += *t;


    return sum;
}



char findTheDifference (char * s, char * t)
{
    int countMap[26] = {0};

    while (*s) {
        countMap[*s++ - 'a']++;
    }

    while (*t) {
        countMap[*t - 'a']--;
        if (countMap[*t - 'a'] < 0) {
            return *t;
        }
        t++;
    }

    return 0;
}


// another solution: sort
