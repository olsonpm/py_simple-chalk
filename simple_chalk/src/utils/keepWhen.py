# ------- #
# Imports #
# ------- #

from .internal.makeCallFn import makeCallFn
from .internal.getTypedResult import getTypedResult


# ---- #
# Init #
# ---- #

moduleName = "keepWhen"


# ---- #
# Main #
# ---- #


def keepWhen(predicate):
    shouldKeep = makeCallFn(predicate, 3, moduleName)

    def keepWhen_inner(collection):
        typedKeepWhen = getTypedResult(collection, _typeToKeepWhen, moduleName)
        return typedKeepWhen(shouldKeep, collection)

    return keepWhen_inner


# ------- #
# Helpers #
# ------- #


def keepWhen_list(shouldKeep, aList):
    result = []
    for idx, el in enumerate(aList):
        if shouldKeep(el, idx, aList):
            result.append(el)

    return result


def keepWhen_dict(shouldKeep, aDict):
    result = {}
    for key, val in aDict.items():
        if shouldKeep(val, key, aDict):
            result[key] = val

    return result


_typeToKeepWhen = {list: keepWhen_list, dict: keepWhen_dict}
