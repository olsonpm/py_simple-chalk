# ------- #
# Imports #
# ------- #

from .internal.makeCallFn import makeCallFn
from .internal.getTypedResult import getTypedResult


# ---- #
# Init #
# ---- #

moduleName = "mMap"


# ---- #
# Main #
# ---- #


def mMap(mapperFn):
    callMapperFn = makeCallFn(mapperFn, 3, moduleName)

    def mMap_inner(collection):
        typedMMap = getTypedResult(collection, _typeToMMap, moduleName)
        return typedMMap(callMapperFn, collection)

    return mMap_inner


# ------- #
# Helpers #
# ------- #


def mMap_list(callMapperFn, aList):
    for idx, el in enumerate(aList):
        aList[idx] = callMapperFn(el, idx, aList)

    return aList


_typeToMMap = {list: mMap_list}
