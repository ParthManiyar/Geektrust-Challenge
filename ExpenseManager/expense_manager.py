from collections import OrderedDict
from typing import List, Tuple

from user import User


class ExpenseManager:
    users = OrderedDict()
    MAXIMUM_USER = 3

    def _validate_user(self, user_name: str) -> None:
        if user_name not in self.users:
            raise Exception("MEMBER_NOT_FOUND")

    def move_in(self, user_name: str) -> str:
        if len(self.users) == self.MAXIMUM_USER:
            raise Exception("HOUSEFUL")
        for user in self.users:
            self.users[user].dues[user_name] = 0
        self.users[user_name] = User(
            balance=0,
            dues={user: 0 for user in self.users}
        )
        return "SUCCESS"

    def _adjust_dues_spend_for(self, spend_by: str, spend_for: str, amount: int) -> int:
        for user in self.users:
            if user != spend_for:
                lent_amount = self.users[user].dues[spend_for]
                if user != spend_by:
                    self.users[user].dues[spend_by] += min(amount, lent_amount)
                self.users[user].dues[spend_for] = max(lent_amount - amount, 0)
                amount = max(amount - lent_amount, 0)
        return amount

    def _adjust_dues_spend_by(self, spend_by: str, spend_for: str, amount: int) -> int:
        for user in self.users[spend_by].dues:
            if user != spend_for:
                due_amount = self.users[spend_by].dues[user]
                self.users[spend_for].dues[user] += min(amount, due_amount)
                self.users[spend_by].dues[user] = max(due_amount - amount, 0)
                amount = max(amount - due_amount, 0)
        return amount

    def _adjust_dues(self, spend_by: str, spend_for: str, amount: int) -> None:
        amount = self._adjust_dues_spend_for(spend_by, spend_for, amount)
        amount = self._adjust_dues_spend_by(spend_by, spend_for, amount)
        self.users[spend_for].dues[spend_by] += amount

    def spend(self, spend_by: str, spend_for: List[str], total_amount: int) -> str:
        self._validate_user(spend_by)
        amount_per_person = round(total_amount/(len(spend_for)+1))
        for member in spend_for:
            self._validate_user(member)
            self.users[member].balance += amount_per_person
            self.users[spend_by].balance -= amount_per_person
            self._adjust_dues(spend_by, member, amount_per_person)
        return "SUCCESS"

    def get_dues(self, user_name: str) -> List[Tuple[str, int]]:
        self._validate_user(user_name)
        dues = self.users[user_name].dues
        output = sorted(dues.items(), key=lambda k: k[1])
        output.reverse()
        return output

    def clear_due(self, owed_by: str, lent_by: str, amount: int) -> str:
        self._validate_user(owed_by)
        self._validate_user(lent_by)
        if self.users[owed_by].dues[lent_by] < amount:
            raise Exception("INCORRECT_PAYMENT")
        self.users[lent_by].balance += amount
        self.users[owed_by].balance -= amount
        self.users[owed_by].dues[lent_by] -= amount
        return str(self.users[owed_by].dues[lent_by])

    def move_out(self, user_name: str) -> str:
        self._validate_user(user_name)
        if self.users[user_name].balance != 0:
            raise Exception("FAILURE")
        del self.users[user_name]
        return "SUCCESS"
