# ------- #
# Imports #
# ------- #

from .internal.makeCallFn import makeCallFn
from .internal.getTypedResult import getTypedResult


# ---- #
# Init #
# ---- #

moduleName = "map_"


# ---- #
# Main #
# ---- #


def map_(mapperFn):
    callMapperFn = makeCallFn(mapperFn, 3, moduleName)

    def map_inner(collection):
        typedMap = getTypedResult(collection, _typeToMap, moduleName)
        return typedMap(callMapperFn, collection)

    return map_inner


# ------- #
# Helpers #
# ------- #


def map_list(callMapperFn, aList):
    result = []
    for idx, el in enumerate(aList):
        result.append(callMapperFn(el, idx, aList))

    return result


_typeToMap = {list: map_list}
