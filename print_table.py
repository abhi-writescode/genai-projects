# Take input
print('Enter a number for which you want to generate a table')
num = int(input('>'))
for i in range(1,11):
    product = num * i
    print(f'{num} x {i} = {product}')