def coords():
    x, y = int(input('Напишите координаты: '))    
    if x >= 1:
        if y >= 1:
            print('I')
    if x <= -1:
        if y <= -1:
            print('III')
    if x >= 1:
        if y <= -1:
            print('IV')
    if x <= -1:
        if y >= 1:
            print('II')


coords()