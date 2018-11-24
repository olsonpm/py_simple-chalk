# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult


# ---- #
# Init #
# ---- #

moduleName = "append"


# ---- #
# Main #
# ---- #


def append(el):
    def append_inner(collection):
        typedAppend = getTypedResult(collection, _typeToAppend, moduleName)
        return typedAppend(el, collection)

    return append_inner


# ------- #
# Helpers #
# ------- #


def append_list(el, aList):
    result = aList.copy().append(el)
    return result


_typeToAppend = {list: append_list}
