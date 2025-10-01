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

print()  # Пустая строка для разделения
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

# Игровая часть - угадывание числа
print()
print("="*40)
print("Ürita ära arvata number vahemikus 0 kuni 20.")

# Загадать число в диапазоне от 0 до 20
target_number = random.randint(0, 20)
guessed = False

while not guessed:
    try:
        userinput = int(input("Sisesta number (0 kuni 20): "))
        
        if userinput == target_number:
            print(f"Õnnitleme! Arvasid õigesti! Numbri {target_number} oli õigesti ära arvatud.")
            guessed = True
        elif userinput < target_number:
            print("Sinu number on liiga väike! Proovi uuesti.")
        else:
            print("Sinu number on liiga suur! Proovi uuesti.")
    
    except ValueError:
        print("Palun sisesta kehtiv number.")
