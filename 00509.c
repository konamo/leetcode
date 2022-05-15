int fib (int n)
{
    if (n == 0)
        return 0;

    if (n == 1)
        return 1;

    int a = 0;
    int b = 1;
    int c;
    for (int ii = 2; ii <= n; ii++) {
        c = a + b;
        a = b;
        b = c;
    }

    return c;
}




// recursive
int fib (int n)
{
    if (n == 0)
        return 0;

    if (n == 1)
        return 1;

    return fib(n - 1) + fib(n - 2);
}
