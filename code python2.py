# Ввод числа от пользователя
userinput = int(input("Sisesta arv: "))

# Подсчет чётных и нечётных чисел от 0 до userinput-1
oddNumber = 0
evenNumber = 0

i = 0
while i < userinput:
    if i % 2 == 0:
        print(i, "paaris arv")
        evenNumber += 1
    else:
        print(i, "paaritu arv")
        oddNumber += 1
    i += 1

print("Paaritute arvude arv:", oddNumber)
print("Paarisarvude arv:", evenNumber)

print("\n" + "="*40 + "\n")

# Демонстрация break
k = 0
while k < 5:
    print("k:", k)
    k += 1
    if k == 3:
        print("Break tingimus")
        break

print("\n" + "="*40 + "\n")

# Демонстрация continue
m = 0
while m < 5:
    if m == 3:
        print("Continue tingimus")
        m += 1
        continue
    print("m:", m)
    m += 1
