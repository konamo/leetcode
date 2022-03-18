class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        e = []
        for ii in tokens:
            if ii not in "+-*/":
                e.append(int(ii))
            else:
                right = e.pop()
                left = e.pop()
                if ii == '+':
                    e.append(left + right)
                elif ii == '-':
                    e.append(left - right)
                elif ii == '/':
                    e.append(int(float(left)/right))
                elif ii == '*':
                    e.append(left * right)

        return e.pop()





def main():
    s = Solution()

    tokens = ["2","1","+","3","*"]
    r = s.evalRPN(tokens)
    print(r)

    tokens = ["4","13","5","/","+"]
    r = s.evalRPN(tokens)
    print(r)

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    r = s.evalRPN(tokens)
    print(r)
    return




if __name__ == '__main__':
    main()
