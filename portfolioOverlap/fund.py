class Fund:
    def __init__(self, name, stocks):
        self.name = name
        self.stocks = stocks

    def add_stock(self, stock):
        self.stocks.append(stock)

    def calculate_overlap(self, fund):
        no_of_common_stocks = 0
        no_of_stocks_in_a = len(self.stocks)
        no_of_stocks_in_b = len(fund.stocks)

        for stocks in fund.stocks:
            if stocks in self.stocks:
                no_of_common_stocks += 1

        percent_overlap = (2 * no_of_common_stocks) * 100
        percent_overlap /= (no_of_stocks_in_a + no_of_stocks_in_b)
        return percent_overlap
