print ('Welcome to temperature convertor')
print ('Enter the value')
t_value = input('>') #input for number
t_value = float(t_value) # convert & reassign
print ('Enter the unit to be converted. Use C for Celsius & F for Fahrenheit') #defining what unit needs to be converted
t_unit = input('>').upper()
str(t_unit)
if t_unit == 'C':
    f_value = (t_value * 9)/5 + 32
    print (f'The temperature in Fahrenheit is {f_value:.2f}')
elif t_unit == 'F':  
    c_value = (t_value - 32)*5/9
    print(f'The temperature in Celsius is {c_value:.2f}')
else:
    print('Wrong Input. Please use C or F')

