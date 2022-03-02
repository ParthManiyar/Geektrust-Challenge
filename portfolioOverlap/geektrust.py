import sys
from utils import get_funds, get_cmd, get_portfolio, read_input, \
    is_calculate_overlap, is_add_stocks, get_fund,  fetch_stock_name


def execute_cmd(funds, portfolio, cmd):
    try:
        op = cmd[0]
        if is_calculate_overlap(op):
            fund_name = cmd[1]
            fund = get_fund(funds, fund_name)
            return portfolio.calculate_overlap(fund)
        elif is_add_stocks(op):
            fund_name = cmd[1]
            fund = get_fund(funds, fund_name)
            stock_name = fetch_stock_name(cmd)
            fund.add_stock(stock_name)
        else:
            return ["INVALID_OPERATION"]
    except Exception as e:
        return [e]
    return []


def main():
    input_file = sys.argv[1]
    funds = get_funds()
    lines = read_input(input_file)
    portfolio = get_portfolio(funds, lines[0])
    lines = lines[1:]
    for line in lines:
        cmd = get_cmd(line)
        output = execute_cmd(funds, portfolio, cmd)
        for i in output:
            print(i)


if __name__ == "__main__":
    main()
