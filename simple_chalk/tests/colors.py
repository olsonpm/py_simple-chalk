# ------- #
# Imports #
# ------- #

from ..src.data import first8Colors, second8Colors
from .. import *  # noqa: F403
from ..src import utils as _
from .utils import makeTestResults


# ---- #
# Main #
# ---- #


def runTests():
    aliasResults = makeTestResults("alias colors")
    foregroundResults = makeTestResults("foreground colors")
    backgroundResults = makeTestResults("background colors")

    aliasResults.errors = testAliases()

    foregroundResults.errors = testColors(first8Colors, 30) + testColors(
        second8Colors, 90
    )

    backgroundResults.errors = testColors(
        first8Colors, 40, isBackground=True
    ) + testColors(second8Colors, 100, isBackground=True)

    return [foregroundResults, backgroundResults, aliasResults]


# ------- #
# Helpers #
# ------- #


def testAliases():
    return (
        testAColor([], "gray", 90, False)
        + testAColor([], "gray", 100, True)
        + testAColor([], "grey", 90, False)
        + testAColor([], "grey", 100, True)
    )


def testAColor(errors, name, code, isBackground):
    if isBackground:
        name = f"bg{_.upperFirst(name)}"

    expected = f"\x1b[{code}msuccess\x1b[0m"
    if globals()[name]("success") != expected:
        errors.append(f'{name}("success")')
    if getattr(chalk, name)("success") != expected:  # noqa: F405
        errors.append(f'chalk.{name}("success")')

    return errors


def testColors(colors, startCode, *, isBackground=False):
    def testAColorWrapper(errors, name, idx):
        return testAColor(errors, name, idx + startCode, isBackground)

    return _.reduce(testAColorWrapper, [])(colors)
