class Portfolio:
    def __init__(self, amount_equity, amount_debt, amount_gold, sip):
        self.__current_equity = amount_equity
        self.__current_debt = amount_debt
        self.__current_gold = amount_gold
        self.__last_rebalance_equity = -1
        self.__last_rebalance_debt = -1
        self.__last_rebalance_gold = -1
        self.__balance_sheet = {}
        self.__initial_allocation_equity = 0
        self.__initial_allocation_debt = 0
        self.__initial_allocation_gold = 0
        self.__sip = sip

    @property
    def total(self):
        return self.__current_equity + self.__current_debt \
               + self.__current_gold

    def calculate_initial_allocation(self):
        self.__initial_allocation_equity = self.__current_equity/self.total
        self.__initial_allocation_debt = self.__current_debt/self.total
        self.__initial_allocation_gold = self.__current_gold/self.total

    def __add_sip(self):
        self.__current_equity += self.__sip.get_equity()
        self.__current_debt += self.__sip.get_debt()
        self.__current_gold += self.__sip.get_gold()

    def __add_market_change(self, change_equity, change_debt, change_gold):
        self.__current_equity += (change_equity * self.__current_equity) / 100
        self.__current_debt += (change_debt * self.__current_debt) / 100
        self.__current_gold += (change_gold * self.__current_gold) / 100
        self.__current_equity = int(self.__current_equity)
        self.__current_debt = int(self.__current_debt)
        self.__current_gold = int(self.__current_gold)

    def __add_month_to_balance_sheet(self, month):
        self.__balance_sheet[month] = {}
        self.__balance_sheet[month]['equity'] = self.__current_equity
        self.__balance_sheet[month]['debt'] = self.__current_debt
        self.__balance_sheet[month]['gold'] = self.__current_gold

    def balance(self, month):
        return self.__balance_sheet[month]

    def __rebalance(self):
        self.__last_rebalance_equity = \
            int(self.total * self.__initial_allocation_equity)
        self.__last_rebalance_debt = \
            int(self.total * self.__initial_allocation_debt)
        self.__last_rebalance_gold = \
            int(self.total * self.__initial_allocation_gold)
        self.__current_equity = self.__last_rebalance_equity
        self.__current_debt = self.__last_rebalance_debt
        self.__current_gold = self.__last_rebalance_gold

    def last_rebalance(self):
        if self.__last_rebalance_gold == -1:
            return "CANNOT_REBALANCE"
        else:
            return str(self.__last_rebalance_equity) \
                   + " " + str(self.__last_rebalance_debt) \
                   + " " + str(self.__last_rebalance_gold)

    def change(self, change_equity, change_debt, change_gold, month):
        if month != "JANUARY":
            self.__add_sip()
        self.__add_market_change(change_equity, change_debt, change_gold)
        if month == "JUNE" or month == "DECEMBER":
            self.__rebalance()
        self.__add_month_to_balance_sheet(month)
