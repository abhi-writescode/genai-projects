# ask user to input a string
print('Enter a string')
og_string = input()
count = len(og_string) # length of the string
rev_string = og_string[::-1] # reverse the string
print(f'The length of the string is {count}')
print(f'The reversered string is {rev_string}')
if rev_string == og_string: # check for palindrome
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')