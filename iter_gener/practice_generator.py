nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(lists):
    len_lists = len(lists)
    index_lists = 0
    index_list = 0

    while len_lists > index_lists:

        yield lists[index_lists][index_list]
        index_list += 1
        if index_list == len(lists[index_lists]):
            index_list = 0
            index_lists += 1


if __name__ == "__main__":

    for item in flat_generator(nested_list):
        print(item)
