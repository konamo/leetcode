class StockSpanner:
    # memorized
    def __init__(self):
        self.prices = []
        self.span = []
        

    def next(self, price: int) -> int:
        days = 1
        while len(self.prices) - days >= 0 and self.prices[-days] <= price:
            days += self.span[-days]

        self.span.append(days)
        self.prices.append(price)

        return days

    # stack
    def __init__(self):
        self.stack = []

    def next(self, price):
        days = 1
        while self.stack and self.stack[-1][0] <= price:
            days += self.stack.pop()[1]
        self.stack.append([price, days])
        return days


    # brute force
    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        days = 1
        for ii in range(len(self.prices) - 1, -1, -1):
            if self.prices[ii] <= price:
                days += 1
            else:
                break
        self.prices.append(price)

        return days
