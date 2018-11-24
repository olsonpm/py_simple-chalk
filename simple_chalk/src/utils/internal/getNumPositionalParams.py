# ------- #
# Imports #
# ------- #

from inspect import Parameter
from math import inf

from .getFnSignature import getFnSignature


# ---- #
# Init #
# ---- #

_nonVarPositionalParamKinds = {
    Parameter.POSITIONAL_ONLY,
    Parameter.POSITIONAL_OR_KEYWORD,
}


# ---- #
# Main #
# ---- #


def getNumPositionalParams(fn, callerName):
    sig = getFnSignature(fn, callerName)

    if _hasVarPositionalParam(sig):
        return inf

    numPositionalParams = 0
    for p in sig.parameters.values():
        if p.kind in _nonVarPositionalParamKinds:
            numPositionalParams += 1

    return numPositionalParams


# ------- #
# Helpers #
# ------- #


def _hasVarPositionalParam(sig):
    for p in sig.parameters.values():
        if p.kind is Parameter.VAR_POSITIONAL:
            return True
