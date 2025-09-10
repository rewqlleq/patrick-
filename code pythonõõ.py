# **Задание 1**: Вычислит сумму, разницу и произведение двух введенных чисел.
esimene_arv = 10  # первое число
teine_arv = 5     # второе число

# Вычисления
summa = esimene_arv + teine_arv
vahe = esimene_arv - teine_arv
korrutis = esimene_arv * teine_arv

# Вывод результатов
print("Задание 1:")
print(f"Сумма: {summa}")
print(f"Разница: {vahe}")
print(f"Произведение: {korrutis}")
print()

# **Задание 2**: Выведет приветствие и предполагаемый год рождения, исходя из возраста пользователя.
nimi = "Martin"       # имя
vanus = 16           # возраст

# Константа текущего года
KAESELEV_AASTA = 2025

# Предполагаемый год рождения
sunniaasta = KAESELEV_AASTA - vanus

# Вывод
print("Задание 2:")
print(f"Привет, {nimi}!")
print(f"Ваш предполагаемый год рождения: {sunniaasta}.")
print()

# **Задание 3**: Поменяет местами два числа без использования дополнительной переменной.
a = 8  # первое число
b = 3  # второе число

# Вывод до обмена
print("Задание 3:")
print(f"До обмена: a = {a}, b = {b}")

# Обмен значениями без дополнительной переменной
a = a + b
b = a - b
a = a - b

# Вывод после обмена
print(f"После обмена: a = {a}, b = {b}")
print()

# **Задание 4**: Преобразует количество секунд в формат времени HH:MM:SS.
sekundid = 3661  # количество секунд

# Преобразование в часы, минуты и секунды
tunnid = sekundid // 3600
minutid = (sekundid % 3600) // 60
sekundid_ule = sekundid % 60

# Вывод результата
print("Задание 4:")
print(f"Время: {tunnid:02}:{minutid:02}:{sekundid_ule:02}")
print()

# **Задание 5**: Сгенерирует билет на рейс с учетом времени вылета и прибытия.
LENDUFIRMA = "NATIONAL AIRLINE"  # название авиакомпании
LAIUS = 40  # ширина билета

lennu_number = "XY123"  # номер рейса
lahte_kood = "TLL"      # код аэропорта вылета
sihtkoha_kood = "HEL"   # код аэропорта назначения
valjumise_aeg = "14:30" # время вылета

# Перевод времени вылета в минуты
tund, minut = map(int, valjumise_aeg.split(":"))
valjumise_minutid = tund * 60 + minut

# Добавление времени прибытия (1 час 45 минут)
saabumise_minutid = valjumise_minutid + 105  # 1 час 45 минут = 105 минут
saabumise_tund = saabumise_minutid // 60
saabumise_minut = saabumise_minutid % 60

# Форматирование времени вылета и прибытия
valjumine_fmt = f"{tund:02}:{minut:02}"
saabumine_fmt = f"{saabumise_tund:02}:{saabumise_minut:02}"

# Генерация билета
print("Задание 5:")
print("*" * LAIUS)
print("*" + LENDUFIRMA.center(LAIUS - 2) + "*")
print("*" + " " * (LAIUS - 2) + "*")
print("*  " + f"Номер рейса: {lennu_number}".ljust(LAIUS - 4) + "*")
print("*" + " " * (LAIUS - 2) + "*")
print("*  " + f"{lahte_kood} -> {sihtkoha_kood}".ljust(LAIUS - 4) + "*")
print("*" + " " * (LAIUS - 2) + "*")
print("*  " + f"Вылет: {valjumine_fmt}    Прибытие: {saabumine_fmt}".ljust(LAIUS - 4) + "*")
print("*" + " " * (LAIUS - 2) + "*")
print("*" * LAIUS)
