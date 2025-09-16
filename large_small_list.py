# ask for inout from user separated by spaces
print('Enter numbers separated by spaces')
numbers = [int(n) for n in input().split()]
numbers.sort()
print(f'The highest number in the list is {numbers[-1]}')
print(f'The lowest number in the list is {numbers[0]}')