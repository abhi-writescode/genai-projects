# ask user to input a number
print('Enter a positive integer')
num = int(input('>'))
fact = 1
if num == 0:
    print(f'Factorial of {num} is 1')
else:
    for i in range (1,num+1):
        fact = i * fact
    print(f'Factorial of {num} is {fact}')