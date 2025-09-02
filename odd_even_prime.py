# Take input
print ('Enter the number')
num = int(input('>'))
# Odd Even check
if num % 2 == 0:
    parity = 'Even'
else:
    parity = 'Odd'
    # Prime check
if num < 2: # 0,1, negatives are not prime
    is_prime = False
else:
    is_prime = True
    for i in range (2, int(num**0.5)+1): # check if input is divisible by numbers till its square root
        if num % i == 0:
            is_prime = False
            break

# Print Result
    if is_prime:
        print(f'The number is {parity} and Prime')
    else:
        print(f'The number is {parity} and Non Prime')

