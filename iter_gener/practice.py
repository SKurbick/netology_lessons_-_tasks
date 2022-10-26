nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


#
class FlatIterator:

    def __init__(self, lists):
        self.lists = lists
        self.lists_index = 0
        self.list_index = -1
        self.len_lists = len(lists)

    def __iter__(self):
        return self

    def __next__(self):

        if len(self.lists[self.lists_index]) == self.list_index + 1:
            if self.len_lists == self.lists_index + 1:
                raise StopIteration
            self.lists_index += 1
            self.list_index = -1

        if len(self.lists[self.lists_index]) > self.list_index + 1:
            self.list_index += 1

        return self.lists[self.lists_index][self.list_index]


if __name__ == '__main__':
    for elem in FlatIterator(nested_list):
        print(elem)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)