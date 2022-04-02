class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = {}
        for index, s in enumerate(secret):
            if s in d:
                d[s].add(index)
            else:
                d[s] = set([index])

        d2 = {}
        for index, s in enumerate(guess):
            if s in d2:
                d2[s].add(index)
            else:
                d2[s] = set([index])


        bulls = 0
        cows = 0
        for k in d.keys():
            if k in d2:
                a = len(d[k] & d2[k])
                bulls += a
                cows += min(len(d[k]), len(d2[k])) - a

        return str(bulls) + 'A' + str(cows) + 'B'


    def getHint2(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bulls, both - bulls)

    def getHint3(self, secret, guess):
        A = sum(a==b for a,b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)





def main():
    s = Solution()
    secret = "1807"
    guess = "7810"
    print(s.getHint(secret, guess))

    secret = "1123"
    guess = "0100"
    print(s.getHint(secret, guess))

    secret = "0123"
    guess = "1144"
    print(s.getHint(secret, guess))
    return



if __name__ == '__main__':
    main()
