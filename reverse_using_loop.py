# Take input from user
print('Enter a string')
input_string = input('>')
reverse_string = "" # Empty string
for char in input_string:
    reverse_string = char + reverse_string
print (f'The reversed string is {reverse_string}')