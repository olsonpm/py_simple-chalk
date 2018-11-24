def invokeAttr(key):
    def invokeAttr_inner(obj):
        return getattr(obj, key)()

    return invokeAttr_inner
