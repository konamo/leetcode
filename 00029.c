// first solution
int divide (int dividend, int divisor)
{
    int64_t result = 0;
    int64_t dividend64 = dividend;
    int64_t divisor64 = divisor;
    int neg = 1;


    if (dividend64 < 0) {
        dividend64 = -dividend64;
        neg *= -1;
    }


    if (divisor64 < 0) {
        divisor64 = -divisor64;
        neg *= -1;
    }

    if (divisor64 == 1) {
        if (dividend64 * neg > INT32_MAX) {
            return INT32_MAX;
        } else if (dividend64 * neg < INT32_MIN) {
            return INT32_MIN;
        }
        return dividend64 * neg;
    }

    while (dividend64 >= divisor64) {
        dividend64 -= divisor64;

        result++;

        if (result * neg > INT32_MAX) {
            return INT32_MAX;
        } else if (result * neg < INT32_MIN) {
            return INT32_MIN;
        }
    }

    return result * neg;
}

// a better solution to shift divisor
int divide (int dividend, int divisor)
{
    int64_t result = 0;
    int64_t dividend64 = dividend;
    int64_t divisor64 = divisor;
    int neg = 1;


    if (dividend64 < 0) {
        dividend64 = -dividend64;
        neg *= -1;
    }


    if (divisor64 < 0) {
        divisor64 = -divisor64;
        neg *= -1;
    }

    while (dividend64 >= divisor64) {
        int64_t t = divisor64;
        int64_t m = 1;

        while ((t << 1) < dividend64) {
            t <<= 1;
            m <<= 1;
        }
        dividend64 -= t;
        result += m;
    }

    if (result * neg > INT32_MAX) {
        return INT32_MAX;
    } else if (result * neg < INT32_MIN) {
        return INT32_MIN;
    }
    return result * neg;
}


// no int64
int divide (int dividend, int divisor)
{
    if (dividend == INT32_MIN && divisor == -1) {
        return INT32_MAX;
    }

    int a = abs(dividend);
    int b = abs(divisor);
    int res = 0;
    int x = 0;

    while (a - b >= 0) {
        for (x = 0; a - (b << (x << 1)) >= 0; x++) {
            ;
        }

        res += 1 << x;
        a -= b << x;
    }

    return (dividend > 0) == (divisor > 0) ? res : -res;
}

// another solution without int64_t
int divide(int dividend, int divisor)
{
    if (dividend == INT_MIN && divisor == -1)
        return INT_MAX;

    int a = abs(dividend);
    int b = abs(divisor);
    int res = 0;

    for (int x = 31; x >= 0; x--) {
        if ((signed)((unsigned)a >> x) - b >= 0) {
            res += 1 << x;
            a -= b << x;
        }
    }

    return (dividend > 0) == (divisor > 0) ? res : -res;
}

int main ()
{
    int x = divide(2147483647, 3);

    printf("%d\n", x);

    return 0;
}
