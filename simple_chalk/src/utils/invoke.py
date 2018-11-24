from .throw import throw


def invoke(aCallable):
    if callable(aCallable):
        return aCallable()
    else:
        throw(ValueError, "'invoke' requires its argument to be callable")
