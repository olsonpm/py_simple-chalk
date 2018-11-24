from .internal.validateStr import validateStr


def upperFirst(maybeString):
    validateStr(maybeString, "upperFirst")
    return maybeString[:1].upper() + maybeString[1:]
