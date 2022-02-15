class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = ''.join(reversed(a))
        b = ''.join(reversed(b))
        index = 0
        carry = 0
        z = []
        while index < len(a) or index < len(b) or carry:
            x = int(a[index]) if index < len(a) else 0
            y = int(b[index]) if index < len(b) else 0

            carry, out = divmod(x + y + carry, 2)
            z.append(out)
            index += 1

        return ''.join([str(c) for c in reversed(z)])

    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        Bitwise implementation
        It can be seen that the XOR algorithm is the same as the addition algorithm, but without carry.
        0 xor 0 = 0
        0 xor 1 = 1
        1 xor 0 = 1
        1 xor 1 = 0 <- without carry

        get carry for AND operation
        0 & 0 = 0
        0 & 1 = 0
        1 & 0 = 0
        1 & 1 = 1 <- carry
        """
        # convert (binary) string to int
        # int(value, base=10)
        m = int(a, 2)
        n = int(b, 2)
        carry = 0

        while n:
            ans = m ^ n

            # shift left here because carry should be 1 bit higher
            carry = (m & n) << 1

            m = ans
            n = carry

        # bin() has '0b' prefix
        return bin(m)[2:]

    def addBinary3(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
            c = [0] * len(b)
        else:
            b = '0' * (len(a) - len(b)) + b
            c = [0] * len(a)

        carry = 0
        for ii in range(len(a) - 1, -1, -1):
            x = int(a[ii])
            y = int(b[ii])

            out = (x + y + carry) % 2
            c[ii] = out
            carry = (x + y + carry) // 2

        if carry:
            c.insert(0, 1)

        return ''.join(str(s) for s in c)

def main():
    s = Solution()
    assert "10101" == s.addBinary("1010", "1011")
    assert "10101" == s.addBinary2("1010", "1011")
    assert "10101" == s.addBinary3("1010", "1011")

    print("Pass")
    return



if __name__ == "__main__":
    main()
