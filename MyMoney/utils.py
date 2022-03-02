from portfolio import Portfolio
from sip import SIP


def sanitize_input(line):
    line = line.split(' ')
    if line[-1][-1] == '\n':
        line[-1] = line[-1][:-1]
    return line


def create_sip(line):
    line = sanitize_input(line)
    equity = float(line[1])
    debt = float(line[2])
    gold = float(line[3])
    sip_obj = SIP(equity, debt, gold)
    return sip_obj


def create_portfolio(line_1, line_2):
    line = sanitize_input(line_1)
    equity = float(line[1])
    debt = float(line[2])
    gold = float(line[3])
    sip_obj = create_sip(line_2)
    portfolio_obj = Portfolio(equity, debt, gold, sip_obj)
    portfolio_obj.calculate_initial_allocation()
    return portfolio_obj


def parse_input_change(line):
    change_equity = float(line[1][:-1])
    change_debt = float(line[2][:-1])
    change_gold = float(line[3][:-1])
    month = line[4]
    return change_equity, change_debt, change_gold, month
