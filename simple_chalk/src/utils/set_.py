def set_(name, value):
    def set_inner(obj):
        setattr(obj, name, value)
        return obj

    return set_inner
