from fund import Fund


class Portfolio:
    def __init__(self, funds):
        self.funds = funds

    def calculate_overlap(self, fund: Fund):
        output = []
        for f in self.funds:
            percent_overlap = fund.calculate_overlap(f)
            if percent_overlap > 0:
                output.append(fund.name + " " + f.name + " " + "{:.2f}".format(
                    round(percent_overlap, 2)) + "%")
        return output
