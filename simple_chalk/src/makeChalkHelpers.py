# ------- #
# Imports #
# ------- #

from .Style import Style
from .utils import flatten, map_, passThrough, reduce, upperFirst


# ---- #
# Main #
# ---- #


def makeStyles(chalkInst, styleInputList):
    def toStyles(result, styleIn):
        name, code, styleType = styleIn
        setattr(type(chalkInst), name, Style(name, str(code), styleType))
        return chalkInst

    return reduce(toStyles, chalkInst)(styleInputList)


def makeOrderedStyles(*, chalkInst, styleListStartCodePairs, styleType):
    return passThrough(
        styleListStartCodePairs,
        [map_(_toStyle(styleType)), flatten, reduce(_toChalk, chalkInst)],
    )


def makePrefixedOrderedStyles(
    *, chalkInst, prefix, styleListStartCodePairs, styleType
):
    prefixedPairs = map_(_addPrefix(prefix))(styleListStartCodePairs)
    return makeOrderedStyles(
        chalkInst=chalkInst,
        styleListStartCodePairs=prefixedPairs,
        styleType=styleType,
    )


# ------- #
# Helpers #
# ------- #


def _toChalk(chalkInst, aStyle):
    setattr(type(chalkInst), aStyle.name, aStyle)
    return chalkInst


def _toStyle(styleType):
    def _toStyle_inner(pair):
        styleList, startCode = pair

        def _makeAStyle(name, idx):
            return Style(name, str(idx + startCode), styleType)

        return map_(_makeAStyle)(styleList)

    return _toStyle_inner


def _addPrefix(prefix):
    def addPrefix_inner(pair):
        styleList, startCode = pair
        styleList = map_(lambda s: prefix + upperFirst(s))(styleList)
        return (styleList, startCode)

    return addPrefix_inner
