#
# README
#  - This is like 'update' except it doesn't overwrite existing keys.  It only
#    assigns new ones.
#


def assignMissing(fromDict):
    def assignMissing_inner(intoDict):
        for k, v in fromDict.items():
            if k not in intoDict:
                intoDict[k] = v

        return intoDict

    return assignMissing_inner
