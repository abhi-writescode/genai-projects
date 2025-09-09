# Ask user to input a string
print('Enter a string')
og_string = input()
count = len(og_string)
rev_string = og_string[::-1]
print(f'The length of the string is {count}')
print(f'The reversered string is {rev_string}')