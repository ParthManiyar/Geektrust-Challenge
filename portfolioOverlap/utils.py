import json
import requests
from fund import Fund
from portfolio import Portfolio

URL_TO_FETCH_FUNDS = "https://geektrust.s3.ap-southeast-1.amazonaws.com/"
URL_TO_FETCH_FUNDS += "portfolio-overlap/stock_data.json"


def get_funds():
    response = requests.get(URL_TO_FETCH_FUNDS)
    data = json.loads(response.content)
    data = data['funds']
    funds = {}
    for fund in data:
        funds[fund['name']] = Fund(fund['name'], fund['stocks'])
    return funds


def get_cmd(line):
    if line[-1] == '\n':
        line = line[:-1]
    cmd = line.split(' ')
    return cmd


def read_input(input_file):
    with open(input_file) as file:
        return file.readlines()


def is_calculate_overlap(op):
    return op == "CALCULATE_OVERLAP"


def is_add_stocks(op):
    return op == "ADD_STOCK"


def get_fund(funds, fund_name):
    if fund_name not in funds:
        raise Exception("FUND_NOT_FOUND")
    return funds[fund_name]


def get_portfolio(funds, line):
    cmd = get_cmd(line)
    fund_names = cmd[1:]
    portfolio_funds = []
    for fund_name in fund_names:
        portfolio_funds.append(funds[fund_name])
    return Portfolio(portfolio_funds)


def fetch_stock_name(cmd):
    return ' '.join(cmd[2:])
