my_list = [1, 4, 5, 63, 3, 4, 5, 0, -1, -2, -3]
print(my_list)

def my_sort(list):
    copied_list = list[:]
    copied_list.sort()
    return copied_list

def my_get_index(list, value):
    return list.index(value)

def my_where(list, predicate):
    return filter(predicate, list)

def min_elements(list, value=5):
    sorted_list = my_sort(list)
    return sorted_list[0:value]

def max_elements(list, value=5):
    sorted_list = my_sort(list)
    return sorted_list[-value:]

print(f'sorted list: {my_sort(my_list)}')
print(f'min 5: {min_elements(my_list, 5)}')
print(f'max 5: {max_elements(my_list, 5)}')
print(f'index: {my_get_index(my_list, 63)}')
print(f'predicate: {list(my_where(my_list, lambda x: x > 1))}')