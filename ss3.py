import random

# Ввод максимального числа с подсказкой, по умолчанию 300
try:
    max_number = int(input("Sisesta maksimaalne arv (vaikimisi 300): "))
except ValueError:
    max_number = 300

print(f"Loendame arvud alates 0 kuni {max_number - 1}...")

# Подсчет четных и нечетных чисел и сумма
odd_count = 0
even_count = 0
total_sum = 0

i = 0
while i < max_number:
    total_sum += i
    if i % 2 == 0:
        print(i, "paaris arv")
        even_count += 1
    else:
        print(i, "paaritu arv")
        odd_count += 1
    i += 1

print()  # пустая строка для разделения
print("Kokku arvude summa:", total_sum)
print("Paaritute arvude arv:", odd_count)
print("Paarisarvude arv:", even_count)

print()
print("="*40)
print()

# Демонстрация break
print("Demonstratsioon: break tingimus")
k = 0
while k < 10:
    print("k:", k)
    k += 1
    if k == 5:
        print("Break tingimus täidetud - tsükkel lõpetatakse")
        break

print()
print("="*40)
print()

# Демонстрация continue
print("Demonstratsioon: continue tingimus")
m = 0
while m < 10:
    if m == 5:
        print("Continue tingimus täidetud - number 5 jäetakse vahele")
        m += 1
        continue
    print("m:", m)
    m += 1

# Игра на угадывание числа с паролем
print()
print("="*40)
print("Ürita ära arvata number vahemikus 0 kuni 20.")

# Пароль для входа
correct_password = "1234"
attempts = 3
logged_in = False

while attempts > 0:
    password = input("Sisesta oma parool: ")
    if password == correct_password:
        print("Parool on õige, tere tulemast!")
        logged_in = True  # Пользователь успешно вошел
        break
    else:
        attempts -= 1
        print(f"Vale parool! Üks katse veel ({attempts} katseid jäänud).")

if not logged_in:
    print("Parooli sisestamine ebaõnnestus. Katkestame programmi.")
else:
    # Игра на угадывание числа от 0 до 20
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
