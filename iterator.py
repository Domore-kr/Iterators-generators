class FlatIterator:
    def __init__(self, some_list: list):
        self.some_list = self.one_lst(some_list)

    def one_lst(self, some_list: list):
        new_list = []
        for item in some_list:
            for i in item:
                new_list.append(i)
        return new_list

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        try:
            self.cursor += 1
            return self.some_list[self.cursor - 1]
        except:
            raise StopIteration