#
# this is only necessary because python's inspect module can't parse the
#   signature of functions written in c - which 'str' is.
#


def toString(something):
    return str(something)
