import unittest

from expense_manager import ExpenseManager
from geektrust import main


class TestAppMethods(unittest.TestCase):
    @staticmethod
    def _expected_outputs():
        return [
            "SUCCESS",
            "SUCCESS",
            "SUCCESS",
            "HOUSEFUL",
            "SUCCESS",
            "SUCCESS",
            "MEMBER_NOT_FOUND",
            "ANDY 1150",
            "WOODY 0",
            "ANDY 850",
            "BO 0",
            "650",
            "INCORRECT_PAYMENT",
            "FAILURE",
            "FAILURE",
            "FAILURE",
            "0",
            "SUCCESS"
        ]

    def test_expense_manager(self):
        ExpenseManager().users.clear()
        actual_output = main("input.txt")
        expected_output = "\n".join(self._expected_outputs())
        self.assertEqual(actual_output, expected_output)

    def test_app(self):
        ExpenseManager().users.clear()
        actual_output = main("input.txt")
        expected_output = "\n".join(self._expected_outputs())
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
