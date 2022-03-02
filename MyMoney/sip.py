class SIP:
    def __init__(self, equity, debt, gold):
        self.__equity = equity
        self.__debt = debt
        self.__gold = gold

    def get_equity(self):
        return self.__equity

    def get_debt(self):
        return self.__debt

    def get_gold(self):
        return self.__gold
