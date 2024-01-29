class Table:
    def __init__(self, list_half=None, dict_half=None):
        if dict_half is None:
            dict_half = {}
        if list_half is None:
            list_half = []
        self.dict = dict_half
        self.list = list_half
        self.length = len(list_half)


def iall(table):
    for i in table.list:
        yield i


def ipairs(table):
    for key, value in table.dict.items():
        yield key, value
