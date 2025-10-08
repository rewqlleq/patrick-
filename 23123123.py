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
            длина = len(tekst.replace(" ", ""))
            print(f"Длина текста без пробелов: {длина}")
    elif valik == "5":
        print("Выход...")
        break
    else:
        print("Неверный выбор, попробуйте снова.")
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
