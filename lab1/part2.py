from functools import reduce

length = int(input('length: '))
numbers = [0] * length

for i in range(len(numbers)):
    numbers[i] = int(input())
print(f'numbers: {numbers}')

odd_numbers = list(filter(lambda n: n % 2 == 1, numbers))
print(f'odd numbers: {odd_numbers}')

product = reduce(lambda n1, n2: n1 * n2, odd_numbers)
print(f'product of numbers: {product}')
