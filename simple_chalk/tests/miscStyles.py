# ------- #
# Imports #
# ------- #

from .. import *  # noqa: F403
from .utils import makeTestResults
from ..src import utils as _


# ---- #
# Init #
# ---- #

miscStyles = [("bold", 1), ("dim", 2), ("underline", 3), ("hidden", 6)]


# ---- #
# Main #
# ---- #


def runTests():
    miscStyleResults = makeTestResults("misc styles")

    miscStyleResults.errors = _.reduce(toResults, [])(miscStyles)

    return [miscStyleResults]


# ------- #
# Helpers #
# ------- #


def toResults(errors, style):
    name, code = style
    expected = f"\x1b[{code}msuccess\x1b[0m"
    if globals()[name]("success") != expected:
        errors.append(f'{name}("success")')
    if getattr(chalk, name)("success") != expected:  # noqa: F405
        errors.append(f'chalk.{name}("success")')

    return errors
