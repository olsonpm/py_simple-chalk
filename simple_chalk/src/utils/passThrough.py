from .reduce import reduce


def passThrough(arg, fnList):
    return reduce(lambda result, fn: fn(result), arg)(fnList)
