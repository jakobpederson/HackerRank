import itertools

def iter_product(list_one, list_two):
    list_of_ints = get_product_as_list(list_one, list_two)
    one_string = get_string_with_no_brackets_from_list(list_of_ints)
    return remove_commas_between_tuples(one_string)

def get_product_as_list(list_one, list_two):
    return list(itertools.product(list_one, list_two))

def get_string_with_no_brackets_from_list(list_of_ints):
    return str(list_of_ints)[1:-1]

def remove_commas_between_tuples(one_string):
    return one_string.replace('),', ')')

def test_iter_product():
    expected = '(1, 3) (1, 4) (2, 3) (2, 4)'
    if expected == iter_product([1, 2], [3, 4]):
        print(True)
    else:
        print('False: {}'.format(iter_product([1, 2], [3, 4])))

m = [int(x) for x in input().split()]
n = [int(x) for x in input().split()]

#test_iter_product()
print(iter_product(m, n))
