from .utils import makeTestResults
from .. import chalk, green


def runTests():
    chainedResults = makeTestResults("chained styles")
    e = chainedResults.errors

    expected = f"\x1b[32;47;1;3msuccess\x1b[0m"
    actual = green.bgWhite.bold.underline("success")
    if actual != expected:
        e.append('green.bgWhite.bold.underline("success")')

    actual = chalk.green.bgWhite.bold.underline("success")
    if actual != expected:
        e.append('chalk.green.bgWhite.bold.underline("success")')

    expected = f"\x1b[31;44;1msuccess\x1b[0m"
    actual = green.bgWhite.bold.bgBlue.red("success")
    if actual != expected:
        e.append('green.bgWhite.bold.bgBlue.red("success")')

    actual = chalk.green.bgWhite.bold.bgBlue.red("success")
    if actual != expected:
        e.append('chalk.green.bgWhite.bold.bgBlue.red("success")')

    return [chainedResults]
