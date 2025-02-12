def ask_password(password):
    count = 0
    while True:
        password1 = input('Введите пароль: ')
        if count != 3:
            if password1 != password:
                count += 1
                print('Неверный пароль! Осталось несколько попыток')
        if count != 3 and password1 == password:
            print('Пароль верный!')
            break
        if count == 3:
            print('Попытки закончились!')
            break
        
ask_password('ezkk')