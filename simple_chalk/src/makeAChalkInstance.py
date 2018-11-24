# ------- #
# Imports #
# ------- #

from .data import first8Colors, second8Colors
from .utils import invoke, passThrough
from .makeAChalkClass import makeAChalkClass
from .makeChalkHelpers import (
    makeStyles,
    makeOrderedStyles,
    makePrefixedOrderedStyles,
)


# ---- #
# Main #
# ---- #


def makeAChalkInstance():
    return passThrough(
        makeAChalkClass(),
        [
            invoke,
            _makeForegroundStyles,
            _makeBackgroundStyles,
            _addAliases,
            _makeNonColorStyles,
        ],
    )


# ------- #
# Helpers #
# ------- #


def _makeForegroundStyles(chalkInst):
    return makeOrderedStyles(
        chalkInst=chalkInst,
        styleListStartCodePairs=[(first8Colors, 30), (second8Colors, 90)],
        styleType="fg",
    )


def _makeBackgroundStyles(chalkInst):
    return makePrefixedOrderedStyles(
        chalkInst=chalkInst,
        prefix="bg",
        styleListStartCodePairs=[(first8Colors, 40), (second8Colors, 100)],
        styleType="bg",
    )


def _addAliases(chalkInst):
    return makeStyles(
        chalkInst,
        [
            ("gray", 90, "fg"),
            ("grey", 90, "fg"),
            ("bgGray", 100, "bg"),
            ("bgGrey", 100, "bg"),
        ],
    )


def _makeNonColorStyles(chalkInst):
    return makeStyles(
        chalkInst,
        [
            ("bold", 1, "bold"),
            ("dim", 2, "dim"),
            ("underline", 3, "underline"),
            #
            # leaving out "blink" (4) and "invert" (5) until a compelling
            #   use-case arises
            #
            ("hidden", 6, "hidden"),
        ],
    )
