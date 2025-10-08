# --- Задание A: Текстовое меню ---

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
        print("Выход...")
        break
    else:
        print("Неверный выбор, попробуйте снова.")
