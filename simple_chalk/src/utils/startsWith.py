from .internal.validateStr import validateStr


def startsWith(prefix):
    validateStr(prefix, "startsWith")

    def startsWith_inner(fullStr):
        validateStr(fullStr, "startsWith_inner")
        return fullStr.startswith(prefix)

    return startsWith_inner
