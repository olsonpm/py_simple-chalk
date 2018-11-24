from ..throw import throw


def validateStr(maybeString, fnName):
    typePassed = type(maybeString)
    if typePassed is not str:
        throw(
            ValueError,
            f"""\
            {fnName} requires a string
            type passed: {typePassed}
            """,
        )
