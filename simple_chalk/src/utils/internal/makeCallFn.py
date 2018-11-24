# ------- #
# Imports #
# ------- #

from math import inf

from .getNumPositionalParams import getNumPositionalParams
from ..throw import throw


# ---- #
# Main #
# ---- #


def makeCallFn(fn, maxParams, callerName):
    numPositionalParams = getNumPositionalParams(fn, callerName)

    if numPositionalParams is inf:
        numPositionalParams = maxParams

    if numPositionalParams > maxParams:
        throw(
            ValueError,
            f"""
            {callerName} can only take functions with up to {maxParams} params
            the function passed '{fn.__name__}' takes {numPositionalParams}
            """,
        )

    return lambda *args: fn(*args[:numPositionalParams])
