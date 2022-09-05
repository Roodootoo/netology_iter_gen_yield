from itertools import chain

print('1. Написать итератор, который принимает список списков, '
      'и возвращает их плоское представление, '
      'т.е последовательность состоящую из вложенных элементов')

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

def flat_generator(main_list):
    for mail_item in main_list:
        for item in mail_item:
            yield item


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

for item in flat_generator(nested_list):
    print(item)
    
gen_nested_list =(x for l in nested_list for x in l)
print(tuple(gen_nested_list))
print('-'*8)

print('3. * Написать итератор аналогичный итератору из задания 1, '
      'но обрабатывающий списки с любым уровнем вложенности')


class FlatIterator8:
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


nested_list8 = [
    ['a', ['b', ['c']]],
    ['d', ['e', ['f', ['h', [False]]]]],
    [1, 2, None]
]
for item in FlatIterator8(nested_list8):
    print(item)

flat_list8 = [item for item in FlatIterator(nested_list8)]
print(flat_list8)
print('-' * 8)


print('4. * Написать генератор аналогичный генератор из задания 2, '
      'но обрабатывающий списки с любым уровнем вложенности')

def flat_generator8(main_list):
    for mail_item in main_list:
        for item in mail_item:
            yield item


nested_list8 = [
    ['a', ['b', ['c']]],
    ['d', ['e', ['f', ['h', [False]]]]],
    [1, 2, None]
]

for item in flat_generator8(nested_list8):
    print(item)

gen_nested_list8 = (x for l in nested_list8 for x in l)
print(tuple(gen_nested_list8))