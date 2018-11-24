# ------- #
# Imports #
# ------- #

from collections import OrderedDict

from .utils import isEmpty, throw


# ---- #
# Main #
# ---- #

#
# I'm wrapping the Chalk class in a factory method for cases where people want
#   their own instance clear of global polution (good for testing)
#
def makeAChalkClass():
    class Chalk:
        def __init__(self):
            setattr(self, "_styleCodes", OrderedDict())

        def _addStyle(self, styleType, code):
            self._styleCodes[styleType] = code
            return self

        def _getCodeList(self):
            return ";".join(self._styleCodes.values())

        def __call__(self, str):
            codeList = self._getCodeList()
            if isEmpty(codeList):
                throw(
                    ValueError,
                    f"""\
                You attempted to call the chalk instance without any styles.
                This is either due to a bug in 'simple_chalk' or you are
                expecting this library to work in a way I didn't intend.  Either
                way I'd appreciate if you raised an issue on github so I can
                prevent others from reaching this.
                    """,
                )

            return f"\x1b[{codeList}m{str}\x1b[0m"

        def _clone(self):
            result = type(self)()
            result._styleCodes.update(self._styleCodes)
            return result

    return Chalk
