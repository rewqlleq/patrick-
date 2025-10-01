import random

# Загадать число в пределах от 0 до 20
target_number = random.randint(0, 20)

print("Ürita ära arvata number vahemikus 0 kuni 20.")

# Загаданный номер
guessed = False

while not guessed:
    try:
        # Ввод числа от пользователя
        userinput = int(input("Sisesta number: "))
        
        if userinput == target_number:
            print(f"Õnnitleme! Arvasid õigesti! Numbri {target_number} oli õigesti ära arvatud.")
            guessed = True
        elif userinput < target_number:
            print("Sinu number on liiga väike! Proovi uuesti.")
        else:
            print("Sinu number on liiga suur! Proovi uuesti.")
    
    except ValueError:
        print("Palun sisesta kehtiv number.")
        
       
        count = 3
        while count != 0:
             userInput  = int(input("Sisesta arv: "))
             if userInput < num:
                print("sa sisestan vähem arv lui oli parem)
                 elif= UserInput == num:
                      print("sa sisestan surem arv kui oli parem)
                       print("sa valisid õge arv")
                     break
             else
print