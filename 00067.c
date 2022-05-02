char * addBinary(char * a, char * b) {
    static char c[50];

    int x = strtol(a, NULL, 2);
    int y = strtol(b, NULL, 2);

    ltoa(x + y, c, 2);
    return c;
}
