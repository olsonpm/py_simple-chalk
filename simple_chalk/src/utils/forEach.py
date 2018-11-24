# ------- #
# Imports #
# ------- #

from .internal.makeCallFn import makeCallFn
from .internal.getTypedResult import getTypedResult


# ---- #
# Init #
# ---- #

moduleName = "forEach"


# ---- #
# Main #
# ---- #


def forEach(fn):
    callFn = makeCallFn(fn, 3, moduleName)

    def forEach_inner(collection):
        typedForEach = getTypedResult(collection, _typeToForEach, moduleName)
        return typedForEach(callFn, collection)

    return forEach_inner


# ------- #
# Helpers #
# ------- #


def forEach_list(callFn, aList):
    for idx, el in enumerate(aList):
        callFn(el, idx, aList)

    return aList


_typeToForEach = {list: forEach_list}
