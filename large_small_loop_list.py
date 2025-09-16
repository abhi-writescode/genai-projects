print('Enter numbers separated by spaces')
numbers = [int(n) for n in input().split()] # convert to integers
# start by assuming first is both min and max
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(f'The highest number in the list is {largest}')
print(f'The lowest number in the list is {smallest}')