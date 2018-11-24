from .. import chalk
from .utils import makeTestResults


def runTests():
    expectedErrorResults = makeTestResults("expected errors")
    e = expectedErrorResults.errors

    try:
        chalk("error")
        e.append('chalk("error")')
    except:
        pass

    return [expectedErrorResults]
