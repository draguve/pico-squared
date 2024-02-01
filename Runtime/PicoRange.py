def pico_range(start, stop, step=1):
    i = start
    while i <= stop:
        yield i
        i += step
