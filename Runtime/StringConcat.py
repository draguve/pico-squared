# TODO make this more performant

def PicoStrConcat(a, b):
    if type(a).__name__ != "bytes":
        a = bytes(str(a), 'utf-8')
    if type(b).__name__ != "bytes":
        b = bytes(str(b), 'utf-8')
    return a+b
