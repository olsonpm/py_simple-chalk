from . import chainedStyles, colors, expectedErrors, miscStyles
from .utils import printResults
from ..src import utils as _


def runTests():
    testModules = [colors, miscStyles, chainedStyles, expectedErrors]

    _.forEach(_runTestModule)(testModules)


def _runTestModule(aTestModule):
    listOfResults = aTestModule.runTests()
    _.forEach(printResults)(listOfResults)
