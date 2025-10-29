print_test_word = lambda: print("test 123")
print_test_word()


get_chetv_stepen_chisla = lambda m: m*m*m*m
print(get_chetv_stepen_chisla(125))


def add(x, y):
    return x + y
add = lambda x, y: x + y
print(add(3, 5))

def _select(lst, condition):
    return [item for item in lst if condition(item)]
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = _select(numbers, lambda x: x % 2 == 0)
print(even_numbers)  