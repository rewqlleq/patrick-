import random

# Начальные данные для логина и пароля
users = {
    'user1': 'password123',  # Логин: user1, Пароль: password123
    'user2': 'qwerty456',    # Логин: user2, Пароль: qwerty456
}

# Проверка логина и пароля
def login():
    print("Palun logige sisse.")
    attempts = 3  # Количество попыток для ввода логина и пароля
    while attempts > 0:
        username = input("Sisesta oma kasutajanimi: ")
        password = input("Sisesta oma parool: ")
        
        if username in users and users[username] == password:
            print(f"Tere tulemast, {username}!")
            return username  # Возвращаем имя пользователя, если логин успешен
        else:
            attempts -= 1
            print(f"Vale kasutajanimi või parool! Katseid jäänud: {attempts}")
    
    print("Parooli sisestamine ebaõnnestus. Katkestame programmi.")
    return None  # Если логин не удается, возвращаем None

# Главное меню с балансом и действиями
def main_menu(username):
    user_balance = 1000  # Начальный баланс пользователя

    while True:
        print("\nVali toiming:")
        print("1. Vaata saldot")
        print("2. Väljasta raha")
        print("3. Lisa raha")
        print("4. Välju")

        choice = input("Sisesta valik (1/2/3/4): ")

        if choice == '1':
            print(f"Teie saldo on: {user_balance} eurot.")
        elif choice == '2':
            try:
                amount = float(input("Kui palju raha soovite välja võtta? "))
                if amount > user_balance:
                    print("Te ei saa võtta rohkem raha, kui teil on kontol.")
                else:
                    user_balance -= amount
                    print(f"Te võtsite välja {amount} eurot. Uus saldo: {user_balance} eurot.")
            except ValueError:
                print("Palun sisesta kehtiv number.")
        elif choice == '3':
            try:
                amount = float(input("Kui palju raha soovite kontole lisada? "))
                user_balance += amount
                print(f"Te lisasite {amount} eurot. Uus saldo: {user_balance} eurot.")
            except ValueError:
                print("Palun sisesta kehtiv number.")
        elif choice == '4':
            print("Aitäh, et kasutasite meie teenuseid!")
            break  # Программа завершится
        else:
            print("Vale valik. Palun proovige uuesti.")

# Игра на угадывание числа от 0 до 20
def guessing_game():
    print("\nÜrita ära arvata number vahemikus 0 kuni 20.")
    num = random.randint(0, 20)
    count = 3  # Количество попыток

    while count != 0:
        try:
            userInput = int(input(f"Sisesta arv (katseid jäänud: {count}): "))

            if userInput < num:
                print("Sinu number on liiga väike! Proovi uuesti.")
            elif userInput > num:
                print("Sinu number on liiga suur! Proovi uuesti.")
            elif userInput == num:
                print(f"Õnnitleme! Arvasid õigesti! Numbri {num} oli õigesti ära arvatud.")
                break  # Завершаем игру, если угадано

        except ValueError:
            print("Palun sisesta kehtiv number.")

        count -= 1  # Уменьшаем количество оставшихся попыток

    # Если попытки закончились
    if count == 0 and userInput != num:
        print(f"Kahjuks, sa ei arvanud õiget numbrit. Õige number oli {num}.")

# Главная часть программы
def main():
    username = login()  # Запрос логина и пароля
    
    if username:
        main_menu(username)  # Если логин успешен, открываем меню
        guessing_game()  # После выхода из меню — игра на угадывание числа
    else:
        print("Programmi lõpp.")  # Если не удалось войти, завершаем программу

if __name__ == "__main__":
    main()
