from .internal.getNumPositionalParams import getNumPositionalParams


def not_(predicate):
    if not callable(predicate):
        raise ValueError("'not' requires its argument to be callable")

    numPositionalParams = getNumPositionalParams(predicate, "not_")

    def not_inner(*args, **kwargs):
        return not predicate(*args[:numPositionalParams], **kwargs)

    return not_inner
