# ------- #
# Imports #
# ------- #

from types import SimpleNamespace as o
from ..src import utils as _


# ---- #
# Init #
# ---- #

_x = "\x1b[31m✘\x1b[0m"
_o = "\x1b[32m✔\x1b[0m"


# ---- #
# Main #
# ---- #


def makeTestResults(label):
    return o(label=label, errors=[])


def printResults(testResults):
    errors = testResults.errors
    label = testResults.label

    if _.isLaden(errors):
        print(label)
        _.forEach(_printAResult)(errors)
    else:
        print(f"{_o} {label}")

    print()


# ------- #
# Helpers #
# ------- #


def _printAResult(result):
    print(f"  {_x} {result}")
