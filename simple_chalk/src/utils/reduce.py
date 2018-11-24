# ------- #
# Imports #
# ------- #

from .internal.makeCallFn import makeCallFn
from .internal.getTypedResult import getTypedResult


# ---- #
# Main #
# ---- #


def reduce(fn, initial):
    reducerFn = makeCallFn(fn, 4, "reduce")

    def reduce_inner(collection):
        typedReduce = getTypedResult(collection, _typeToReduce, "reduce")
        return typedReduce(reducerFn, initial, collection)

    return reduce_inner


# ------- #
# Helpers #
# ------- #


def reduce_list(reducerFn, initial, aList):
    result = initial
    for idx, el in enumerate(aList):
        result = reducerFn(result, el, idx, aList)

    return result


_typeToReduce = {list: reduce_list}
