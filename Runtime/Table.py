class Table:
    def __init__(self, list_half=None, dict_half=None):
        if dict_half is None:
            dict_half = {}
        if list_half is None:
            list_half = []
        self.dict = dict_half
        self.list = list_half

    def __getitem__(self, item):
        if isinstance(o, bytes):
            return self.dict.get(item, None)
        else:
            idx = int(item)
            if 1 <= idx <= len(self.list) + 1:
                return self.list[idx - 1]
            else:
                return self.dict.get(item, None)

    def __setitem__(self, key, value):
        if isinstance(key, bytes):
            self.dict[key] = value
        else:
            idx = int(key)
            if idx == len(self.list) + 1:
                self.list.append(value)
                if key in self.dict:
                    del self.dict[key]
            else:
                self.dict[key] = value

    def __len__(self):
        return len(self.list)


def iall(table):
    for i in table.list:
        yield i


def ipairs(table):
    for key, value in table.dict.items():
        yield key, value
