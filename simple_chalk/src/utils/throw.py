from textwrap import dedent


def throw(errorClass, message, *, fromException=None):
    if fromException is None:
        raise errorClass(dedent(message))
    else:
        raise errorClass(dedent(message)) from fromException
