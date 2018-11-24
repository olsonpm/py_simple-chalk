class Style:
    def __init__(self, name, code, styleType):
        self.name = name
        self.code = code
        self.styleType = styleType

    def __get__(self, instance, _owner):
        result = instance._clone()
        result._addStyle(self.styleType, self.code)
        return result

    def __set__(self, instance, value):
        raise AttributeError(f"the attribute '{self.name}' cannot be set")
