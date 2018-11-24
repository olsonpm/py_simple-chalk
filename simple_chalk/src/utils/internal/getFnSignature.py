from inspect import signature
from ..throw import throw


def getFnSignature(fn, callerName):
    try:
        return signature(fn)
    except Exception as e:
        throw(
            ValueError,
            f"""\
            '{callerName}' is unable to get the signature of the passed callable
            callable passed: {repr(fn)}

            one reason this could occur is the callable is written in c (e.g.
            the builtin 'str' callable).
            """,
            fromException=e,
        )
