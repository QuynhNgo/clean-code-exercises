# This code allows you to store information on people owing you money
# and then list all those people in a ordered and formatted way in the terminal.
# Try to improve the `payday` function by splitting the logic into smaller functions.

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Debtor:
    """Stores the information on a person owing us money"""
    name: str
    debt: float


def sort_debtor(debtors: Iterable[Debtor]) -> list:
    # First, we sort the debtors according to their debt
    # such that those with the highest debt are printed first
    ordered = reversed(sorted(debtors, key=lambda debtor: debtor.debt))
    return ordered

def print_debtor(debtors: Iterable[Debtor]) -> None:
    # Then we print the debtors, highlighting debts above 100 by exclamation marks
    for debtor in debtors:
        if debtor.debt > 100.0:
            print(f"{debtor.name}: !!!{debtor.debt}!!!")
        else:
            print(f"{debtor.name}: {debtor.debt}")


if __name__ == "__main__":
    sortDeptors = sort_debtor([
        Debtor("Person1", 100.0),
        Debtor("Person2", 200.0),
        Debtor("Person3", 10.0),
        Debtor("Person4", 50.0),
        Debtor("Person5", 1250.0)
    ])
    print_debtor(sortDeptors)
