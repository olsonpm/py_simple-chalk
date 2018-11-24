from .internal.validateStr import validateStr


def lowerFirst(maybeString):
    validateStr(maybeString, "lowerFirst")
    return maybeString[:1].lower() + maybeString[1:]
