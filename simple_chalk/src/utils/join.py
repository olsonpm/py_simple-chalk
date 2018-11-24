# ------- #
# Imports #
# ------- #

from .internal.getTypedResult import getTypedResult


# ---- #
# Main #
# ---- #


def join(separator):
    def join_inner(collection):
        typedJoin = getTypedResult(collection, _typeToJoin, "join")
        return typedJoin(separator, collection)

    return join_inner


# ------- #
# Helpers #
# ------- #


def join_list(separator, aList):
    return separator.join(aList)


_typeToJoin = {list: join_list}
