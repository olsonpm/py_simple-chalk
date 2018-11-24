from types import SimpleNamespace as o

#
# README
#  - I have no idea what to name this.  Python just doesn't have a clean ternary
#    operator which stinks and I didn't want to use 'iif' because that's
#    unreadable.  So for now we have a verbose and less performant, but readable
#    function chain
#


def whenTruthy(condition):
    def return_(truthyResult):
        def otherwise(falseyResult):
            if condition:
                return truthyResult
            else:
                return falseyResult

        return o(otherwise=otherwise)

    return o(return_=return_)
