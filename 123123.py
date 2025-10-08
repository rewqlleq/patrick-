# -----------------------------------
# Задание A) Текстовое меню с while
# -----------------------------------

print("\n--- Задание A: Текстовое меню ---")

tekst = ""

while True:
    print("\nМеню:")
    print("1. Введите текст")
    print("2. Удалить пробелы с краев (strip)")
    print("3. Удалить лишние пробелы")
    print("4. Показать длину без пробелов")
    print("5. Выйти")

    valik = input("Выберите действие (1-5): ")

    if valik == "1":
        tekst = input("Введите текст: ")
    elif valik == "2":
        if tekst == "":
            print("Сначала введите текст.")
        else:
            tekst = tekst.strip()
            print(f"Текст после удаления пробелов: '{tekst}'")
    elif valik == "3":
        if tekst == "":
            print("Сначала введите текст.")
        else:
            while "  " in tekst:
                tekst = tekst.replace("  ", " ")
            print(f"Текст после удаления лишних пробелов: '{tekst}'")
    elif valik == "4":
        if tekst == "":
            print("Сначала введите текст.")
        else:
            pikkus = len(tekst.replace(" ", ""))
            print(f"Длина текста без пробелов: {pikkus}")
    elif valik == "5":
        print("Выход из меню.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")

# -----------------------------------
# Задание B) Проверка имени пользователя
# -----------------------------------

print("\n--- Задание B: Проверка имени пользователя ---")

while True:
    username = input("Введите имя пользователя (4-12 символов, только буквы и цифры): ")
    
    if len(username) < 4 or len(username) > 12:
        print("Имя пользователя должно быть от 4 до 12 символов.")
    elif not username.isalnum():
        print("Имя пользователя должно содержать только буквы и цифры.")
    elif " " in username:
        print("Имя пользователя не может содержать пробелы.")
    else:
        print("Имя пользователя корректно!")
        break

# -----------------------------------
# Задание C) Нормализация имени
# -----------------------------------

print("\n--- Задание C: Нормализация имени ---")

while True:
    nimi = input("Введите имя (например, F/N или F/N/P): ").strip()
    
    # Удаляем лишние пробелы
    nimi = " ".join(nimi.split())
    
    osad = nimi.split()
    
    if len(osad) < 2:
        print("Введите хотя бы имя и фамилию.")
    else:
        nimi = " ".join([osa.title() for osa in osad])
        print(f"Нормализованное имя: {nimi}")
        break

# -----------------------------------
# Задание A) Sanitizer строки (for)
# -----------------------------------

print("\n--- Задание A (for): Sanitizer строки ---")

tekst = "  annA\tIVAN  \n oLEg "
puhas_tekst = ""
prev_space = False

for char in tekst:
    if char.isalnum() or char == " ":
        if char == " ":
            if prev_space:
                continue
            prev_space = True
        else:
            prev_space = False
        puhas_tekst += char
    elif char in ["\t", "\n"]:
        if not prev_space:
            puhas_tekst += " "
            prev_space = True
    else:
        continue

print(f"Исходный текст: {tekst}")
print(f"Почищенный текст: {puhas_tekst.strip()}")

# -----------------------------------
# Задание B) Подсчет строк
# -----------------------------------

print("\n--- Задание B: Подсчет строк ---")

read = 0
tuhjad = 0
luhikesed = 0

while True:
    rida = input("Введите строку (пустая строка для завершения): ")
    if rida == "":
        break
    
    read += 1
    rida = rida.strip()
    
    if rida == "":
        tuhjad += 1
    elif len(rida) < 5:
        luhikesed += 1

print(f"Всего строк: {read}")
print(f"Пустых строк: {tuhjad}")
print(f"Коротких строк (<5 символов): {luhikesed}")

# -----------------------------------
# Задание C) Генератор приветствий из списка (while без split)
# -----------------------------------

print("\n--- Задание C: Генератор приветствий ---")

nimed_str = "  annA,IVAN ,  oLEg  "
nimed_str = nimed_str.strip()

i = 0
nimi = ""

while i < len(nimed_str):
    if nimed_str[i] == ",":
        if nimi.strip():
            print(f"Hello, {nimi.title()}!")
        nimi = ""
    else:
        nimi += nimed_str[i]
    i += 1

if nimi.strip():
    print(f"Hello, {nimi.title()}!")
