import sys

from utils import read_file, is_dues, is_move_in, is_move_out, is_spend, is_clear_due
from expense_manager import ExpenseManager


def main(input_file: str = None) -> str:
    if not input_file:
        input_file = sys.argv[1]
    cmds = read_file(input_file)
    temp_arr = []
    for cmd in cmds:
        cmd = cmd.split()
        try:
            if is_move_in(cmd):
                temp_arr.append(ExpenseManager().move_in(user_name=cmd[1]))
            elif is_spend(cmd):
                temp_arr.append(ExpenseManager().spend(
                                                    spend_by=cmd[2],
                                                    spend_for=cmd[3:],
                                                    total_amount=int(cmd[1])))
            elif is_dues(cmd):
                output = ExpenseManager().get_dues(user_name=cmd[1])
                for line in output:
                    temp_arr.append(f"{line[0]} {line[1]}")
            elif is_clear_due(cmd):
                temp_arr.append(ExpenseManager().clear_due(
                                                  owed_by=cmd[1],
                                                  lent_by=cmd[2],
                                                  amount=int(cmd[3])))
            elif is_move_out(cmd):
                temp_arr.append(ExpenseManager().move_out(user_name=cmd[1]))
        except Exception as e:
            temp_arr.append(str(e))
    return "\n".join(temp_arr)


if __name__ == "__main__":
    print(main())
