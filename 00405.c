char * toHex(int num)
{
    char *hex = (char*)malloc(32);


    sprintf(hex, "%x", num);

    return hex;
}


char * toHex(int num)
{
    char *hex = (char*)malloc(11);
    int ii = 0;
    char c;
    int t;
    uint32_t n = num;
    const char *HEX = "0123456789abcdef";


    if (!hex) {
        return NULL;
    }

    if (n == 0) {
        return "0";
    }

    while (n) {
        hex[ii++] = HEX[n & 0xf];
        n >>= 4;
    }
    hex[ii] = 0;

    //swap
    for (int jj = 0; jj < ii / 2; jj++) {
        c = hex[jj];
        hex[jj] = hex[ii - jj - 1];
        hex[ii - jj - 1] = c;
    }

    return hex;
}
