import unittest
from geektrust import execute_cmd
from utils import get_funds, get_portfolio, get_cmd


class TestAppMethods(unittest.TestCase):

    def test_app(self):
        lines = ["", "", "", "", "", ""]
        lines[0] = "CURRENT_PORTFOLIO UTI_NIFTY_INDEX AXIS_MIDCAP PARAG_PARIKH_FLEXI_CAP"
        lines[1] = "CALCULATE_OVERLAP ICICI_PRU_NIFTY_NEXT_50_INDEX"
        lines[2] = "CALCULATE_OVERLAP NIPPON_INDIA_PHARMA_FUND"
        lines[3] = "ADD_STOCK PARAG_PARIKH_FLEXI_CAP NOCIL"
        lines[4] = "ADD_STOCK AXIS_MIDCAP NOCIL"
        lines[5] = "CALCULATE_OVERLAP ICICI_PRU_NIFTY_NEXT_50_INDEX"
        olines = ["", "", "", "", "", "", ""]
        olines[0] = "ICICI_PRU_NIFTY_NEXT_50_INDEX UTI_NIFTY_INDEX 20.37%"
        olines[1] = "ICICI_PRU_NIFTY_NEXT_50_INDEX AXIS_MIDCAP 14.81%"
        olines[2] = "ICICI_PRU_NIFTY_NEXT_50_INDEX PARAG_PARIKH_FLEXI_CAP 7.41%"
        olines[3] = "FUND_NOT_FOUND"
        olines[4] = "ICICI_PRU_NIFTY_NEXT_50_INDEX UTI_NIFTY_INDEX 20.37%"
        olines[5] = "ICICI_PRU_NIFTY_NEXT_50_INDEX AXIS_MIDCAP 14.68%"
        olines[6] = "ICICI_PRU_NIFTY_NEXT_50_INDEX PARAG_PARIKH_FLEXI_CAP 7.32%"
        i = 0
        funds = get_funds()
        portfolio = get_portfolio(funds, lines[0])
        lines = lines[1:]
        for line in lines:
            cmd = get_cmd(line)
            output = execute_cmd(funds, portfolio, cmd)
            for o in output:
                self.assertEqual(olines[i], str(o))
                i += 1


if __name__ == '__main__':
    unittest.main()
