cat_names = []
while True:
    print('Enter name of the cat' + str(len(cat_names)+1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name] #List concatenation
    print('The names of the cat are:')
    for name in cat_names:
        print('' + name)