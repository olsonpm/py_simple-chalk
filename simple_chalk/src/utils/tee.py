def tee(msg):
    return lambda something: print(msg) or print(something) or something
