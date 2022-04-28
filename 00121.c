#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int maxProfit (int* prices, int pricesSize)
{
    int buy = 0, sell = 1;
    int profit = 0;

    while (sell < pricesSize) {
        if (prices[buy] < prices[sell]) {
            profit = MAX(profit, prices[sell] - prices[buy]);
        } else {
            buy = sell;
        }
        sell++;
    }

    return profit;
}

int maxProfit (int* prices, int pricesSize)
{
    int buy, sell;
    int profit = 0;

    for (buy = 0; buy < pricesSize - 1; buy++) {
        for (sell = buy + 1; sell < pricesSize; sell++) {
            profit = MAX(profit, prices[sell] - prices[buy]);
        }
    }

    return profit;
}

int maxProfit (int* prices, int pricesSize)
{
    int buy = 0, sell;
    int profit = 0;

    for (sell = buy + 1; sell < pricesSize; sell++) {
        if (prices[buy] < prices[sell]) {
            profit = MAX(profit, prices[sell] - prices[buy]);
        } else {
            buy = sell;
        }
    }

    return profit;
}



int main()
{
    return 0;
}
