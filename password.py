def ask_password(password):
    count = 0
    while password != password:
        if password != password:
            count += 1
            print('Неверный пароль! Осталось несколько попыток')
        if count == 3:
            print('Попытки закончились!')