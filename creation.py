"""This module contains the function: bin_dict_maker(keys, types, options, file, size=15)

bin_dict_maker creates binary files whose contents are dictionaries with appropriate keys and values

The keys parameter accepts list of string type values that would be the keys of the new dictionary
The types parameter accepts list of key types with 1:int and 2:str
The options parameter accepts list of optional values. these have a 50% chance of appearing as values
The file parameter accepts file name/path as string
The optional parameter accepts the number of dictionaries to be created. Default = 15"""

import random
import pickle
from string import ascii_letters


# noinspection PyTypeChecker,PyTypeChecker,PyUnusedLocal
def bin_dict_maker(keys, types, options, file, size=15):
    with open(file + '.dat', 'wb') as w_file:
        storage = tuple()

        for _ in range(size):
            lst = [None for _ in range(10)]

            # data manipulation part
            keys = [k for k in keys if k]
            for element in (types, options):
                element = [element[v] for v in range(1, len(keys))]

            if random.choice((True, False)):
                for i in range(len(keys)):  # for optional data
                    if options[i] != '':
                        if types[i] == 2:
                            lst[i] = options[i]
                        else:
                            lst[i] = eval(options[i])

            for i in range(len(keys)):  # for random data
                if lst[i] is None:
                    if types[i] == 2:
                        lst[i] = ''.join(random.sample(ascii_letters, 5))
                    else:
                        lst[i] = random.randrange(1, 101)
            dic = dict(zip(keys, lst))
            storage += (dic, )
            pickle.dump(dic, w_file)

        return storage


if __name__ == '__main__':
    file_ = input('enter file name without extension: ')
    key = input('enter list of keys as space delimited values: ')
    type_ = input('enter list of types as space delimited values: ')
    opt = input('enter list of optional values as space: delimited values: ')

    bin_dict_maker(key, type_, opt, file_)

    try:
        with open(file_ + '.dat', 'rb') as r_file:
            while True:
                a = pickle.load(r_file)
                print(a)
    except EOFError:
        pass
