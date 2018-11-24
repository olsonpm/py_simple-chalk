def get(attrName):
    def get_inner(something):
        return getattr(something, attrName)

    return get_inner
