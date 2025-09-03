print("hello world 1")
print("1" + "1")
#print(1+2) # keelatud
#"hello world" - str
#1 - int
#1.5 - float

# muutujad
name = "Beyond"
perekonanimi = "birthday"
print(name + " " + perekonanimi)

# luua muutujad film, aasta, rezisöör ja näitlejad
film = "Dexter"
year = 2006
rezisoor = "James Manos Jr."
naitleja1 = "Micheal C. Hall"
naitleja2 = "Cristian Camargo"

print(f"Film {film} ilmus aastal {year}, rezissöör on {rezisoor}, ning peanäitlejad on {naitleja1} ja {naitleja2}.")

# lemmikloom
lemmikloom = input("Hunt: ")
print("Lemmik loom: " + lemmikloom)

# ristküliku arvutused
pikkus = int(input("Sisesta pikkus: "))
laius = int(input("Sisesta laius: "))

umbermoot = 2 * (pikkus + laius)
pindala = pikkus * laius

print("Ümbermõõt:", umbermoot)
print("Pindala:", pindala)
print("Laius:", laius)

# andmete küsimine
nimi = input("Sisesta oma nimi: ")
elukoht = input("Miami Beach : ")
lemmikfilm = input("Sisesta oma lemmikfilm: ")
lemmikmuusika = input("Sisesta oma lemmikmuusika: ")
toit1 = input("pitsa: ")
toit2 = input("sushi: ")
toit3 = input("puder: ")

print(f"Tere, minu nimi on {nimi}.")
print(f"Ma elan {elukoht}.")
print(f"Minu lemmikfilm on {lemmikfilm}, ning mulle meeldib {lemmikmuusika}.")
print(f"Minu lemmiktoidud on {toit1}, {toit2} ja {toit3}.")

