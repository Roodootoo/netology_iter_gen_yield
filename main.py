from itertools import chain

# '1. Написать итератор, который принимает список списков, '
# 'и возвращает их плоское представление, '
# 'т.е последовательность состоящую из вложенных элементов')
class FlatIterator:
    def __init__(self, list):
        self.main_list = list

    def __iter__(self):
        self.main_cursor = 0
        self.nested_cursor = -1
        return self

    def __next__(self):
        self.nested_cursor += 1
        if self.nested_cursor == len(self.main_list[self.main_cursor]):
            self.main_cursor += 1
            self.nested_cursor = 0
            if self.main_cursor == len(self.main_list):
                raise StopIteration
        return self.main_list[self.main_cursor][self.nested_cursor]


# '2. Написать генератор, который принимает список списков, '
# 'и возвращает их плоское представление'
def flat_generator(main_list):
    for mail_item in main_list:
        for item in mail_item:
            yield item


# '3. * Написать итератор аналогичный итератору из задания 1, '
# 'но обрабатывающий списки с любым уровнем вложенности'
class FlatIteratorRecurse:
    def __init__(self, list):
        self.main_list = list

    # Пыталась пыталась и не дошло до конца... сделала через доп функцию)
    def merge(self, main_list, res=[]):
        for item in main_list:
            self.merge(item) if isinstance(item, list) else res.append(item)
        return res

    def __iter__(self):
        self.main_cursor = -1
        self.iterator = iter(self.main_list)
        self.merge_ = self.merge(self.main_list)
        return self

    def __next__(self):
        self.main_cursor += 1
        if self.main_cursor == len(self.merge_):
            raise StopIteration
        return self.merge_[self.main_cursor]
        # ...наработки...
        # self.next_iter = next(self.iterator)
        # if isinstance(self.next_iter, list):
        #     FlatIteratorRecurse(self.next_iter)
        # else:
        #     self.main_cursor += 1
        #     if self.main_cursor == len(self.main_list):
        #         raise StopIteration
        #     return self.next_iter


# '4. * Написать генератор аналогичный генератор из задания 2, '
# 'но обрабатывающий списки с любым уровнем вложенности'
def flat_generator_recurse(main_list):
    for main_item in main_list:
        if isinstance(main_item, list):
            for sub_item in flat_generator_recurse(main_item):
                yield sub_item
        else:
            yield main_item



if __name__ == '__main__':

    print('1. Написать итератор, который принимает список списков, '
          'и возвращает их плоское представление, '
          'т.е последовательность состоящую из вложенных элементов')
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('-'*8)


    print('2. Написать генератор, который принимает список списков, '
      'и возвращает их плоское представление')

    for item in flat_generator(nested_list):
        print(item)

    gen_nested_list =(x for l in nested_list for x in l)
    print(tuple(gen_nested_list))
    print('-'*8)


    print('3. * Написать итератор аналогичный итератору из задания 1, '
          'но обрабатывающий списки с любым уровнем вложенности')

    nested_list8 = [
        ['a', ['b', ['c']], 'd'],
        ['e', ['f', ['h', ['j', [False]],1]]],
        [2, 3, None],[[[4]]]
    ]

    for item in FlatIteratorRecurse(nested_list8):
        print(item)
    print('-' * 8)


    print('4. * Написать генератор аналогичный генератор из задания 2, '
          'но обрабатывающий списки с любым уровнем вложенности')
    for item in flat_generator_recurse(nested_list8):
        print(item)
