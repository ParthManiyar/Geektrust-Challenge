import sys
from utils import create_portfolio, parse_input_change, sanitize_input
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def requests_retry_session(
    retries=1,
    status_forcelist=(500, 502, 503, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def main():
    print(requests_retry_session().get("https://googlel.com", timeout=10))
    input_file = sys[1].argv
    with open(input_file) as f:
        line_1 = f.readline()
        line_2 = f.readline()
        portfolio_obj = create_portfolio(line_1, line_2)
        lines = f.readlines()
        for line in lines:
            line = sanitize_input(line)
            if line[0] == 'CHANGE':
                change_equity, change_debt, change_gold, month = \
                    parse_input_change(line)
                portfolio_obj.change(change_equity, change_debt, change_gold,
                                     month)
            elif line[0] == 'BALANCE':
                month = line[1]
                balance = portfolio_obj.balance(month)
                print(str(int(balance['equity']))
                      + " " + str(int(balance['debt']))
                      + " " + str(int(balance['gold'])))
            elif line[0] == 'REBALANCE':
                print(portfolio_obj.last_rebalance())


if __name__ == "__main__":
    main()
