# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult


# ---- #
# Init #
# ---- #

moduleName = "appendAll"


# ---- #
# Main #
# ---- #


def appendAll(collectionToAppend):
    def appendAll_inner(collection):
        typedAppendAll = getTypedResult(
            collection, _typeToAppendAll, moduleName
        )
        return typedAppendAll(collectionToAppend, collection)

    return appendAll_inner


# ------- #
# Helpers #
# ------- #


def appendAll_list(listToAppend, aList):
    return aList + listToAppend


_typeToAppendAll = {list: appendAll_list}
