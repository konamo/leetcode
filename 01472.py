class BrowserHistory2:

    def __init__(self, homepage: str):
        self.url = [homepage]
        self.curr = 0
        

    def visit(self, url: str) -> None:
        if len(self.url) - 1 > self.curr:
            self.url[self.curr + 1] = url
            self.curr += 1
            while len(self.url) - 1 > self.curr:
                self.url.pop()
        else:
            self.url.append(url)
            self.curr += 1
        

    def back(self, steps: int) -> str:
        self.curr -= steps
        if self.curr < 0:
            self.curr = 0
        return self.url[self.curr]
        

    def forward(self, steps: int) -> str:
        self.curr += steps
        if self.curr >= len(self.url):
            self.curr = len(self.url) - 1
        return self.url[self.curr]
        

class BrowserHistory2:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []
        

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while steps and len(self.history) > 1:
            self.future.append(self.history.pop())
            steps -= 1
        return self.history[-1]
        

    def forward(self, steps: int) -> str:
        while steps and self.future:
            self.history.append(self.future.pop())
            steps -= 1
        return self.history[-1]


class BrowserHistory3:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.pos += 1
        self.history = self.history[:self.pos]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos - steps)
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(len(self.history) - 1, self.pos + steps)
        return self.history[self.pos]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

["BrowserHistory","visit","visit","back","visit","forward","visit","visit","forward","visit","back","visit","visit","forward"]

[["esgriv.com"],["cgrt.com"],["tip.com"],[9],["kttzxgh.com"],[7],["crqje.com"],["iybch.com"],[5],["uun.com"],[10],["hci.com"],["whula.com"],[10]]


def main():
    h = BrowserHistory("esgriv")
    h.visit("cgrt")
    h.visit("tip")
    print(h.back(9))
    h.visit("kttzxgh")
    print(h.forward(7))
    h.visit("crqje")
    h.visit("iybch")
    h.forward(5)
    h.visit("uun")
    h.back(10)
    h.visit("hci")
    h.visit("whula")
    h.forward(10)

    return



if __name__ == '__main__':
    main()
