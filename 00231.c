bool isPowerOfTwo (int n) {

    // check number of 1 bits
    // true == number of 1 bit is 1
    int ii;
    int count = 0;


    if (n < 0) {
        return false;
    }

    for (ii = 0; ii < 32; ii++) {
        if (n & 0x1) {
            count++;
            if (count > 1) {
                return false;
            }
        }
        n >>= 1;
    }

    if (count == 1) {
        return true;
    }
    return false;
}


bool isPowerOfTwo (int n) {
    if (n <= 0) {
        return false;
    }

    while (n > 1) {
        if (n % 2) {
            return false;
        }
        n /= 2;
    }

    return true;
}
