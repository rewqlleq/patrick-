import random

# Загадать число
max_number = 300  # Например, установим максимальное значение в 300
target_number = random.randint(0, max_number - 1)

print(f"Ürita ära arvata number vahemikus 0 kuni {max_number - 1}.")

# Загаданный номер
guessed = False

while not guessed:
    userinput = int(input("Sisesta number: "))
    
    if userinput == target_number:
        print(f"Õnnitleme! Arvasid õigesti! Numbri {target_number} oli õigesti ära arvatud.")
        guessed = True
    elif userinput < target_number:
        print("Sinu number on liiga väike! Proovi uuesti.")
    else:
        print("Sinu number on liiga suur! Proovi uuesti.")
