from typing import List


def read_file(file_path: str) -> List[str]:
    with open(file_path) as file:
        return file.readlines()


def is_move_in(cmd) -> bool:
    return cmd[0] == "MOVE_IN"


def is_spend(cmd) -> bool:
    return cmd[0] == "SPEND"


def is_dues(cmd) -> bool:
    return cmd[0] == "DUES"


def is_clear_due(cmd) -> bool:
    return cmd[0] == "CLEAR_DUE"


def is_move_out(cmd) -> bool:
    return cmd[0] == "MOVE_OUT"
