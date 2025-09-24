print("Ülesanne 1: päevaaja määramine tunni järgi")
hour = int(input("Sisesta tund (0-23): "))
if 0 <= hour < 6:
    print("Öö")
elif 6 <= hour < 12:
    print("Hommik")
elif 12 <= hour < 18:
    print("Päev")
elif 18 <= hour < 24:
    print("Õhtu")
else:
    print("Vale tund")


print("\nÜlesanne 2: joogi valik eelistuse järgi")
preference = input('Sisesta joogi eelistus ("kuum" või "külm"): ')
if preference == "kuum":
    print("Kohv")
elif preference == "külm":
    print("Limonaad")
else:
    print("Tundmatu eelistus")


print("\nÜlesanne 3: riietuse värvi kontroll")
color = input('Sisesta värv ("punane", "sinine" või muu): ')
if color == "punane":
    print("Ere")
elif color == "sinine":
    print("Rahulik")
else:
    print("Tavaline")


print("\nÜlesanne 4: marsruudi valik transpordi ja ilma järgi")
transport = input('Sisesta transport ("buss" või "jalgsi"): ')
weather = input('Sisesta ilm ("vihm" või "päike"): ')

if transport == "buss" and weather == "vihm":
    print("Sõidame bussiga katuse all")
elif transport == "buss" and weather == "päike":
    print("Sõidame bussiga mugavalt")
elif transport == "jalgsi" and weather == "vihm":
    print("Võtame vihmavarju")
elif transport == "jalgsi" and weather == "päike":
    print("Kõnnime rõõmsalt")
else:
    print("Tundmatu valik")


print("\nÜlesanne 5: toidu klassifitseerimine tüübi ja maitse järgi")
type_ = input('Sisesta tüüp ("puuvili" või "köögivili"): ')
taste = input('Sisesta maitse ("magus", "hapu" või muu): ')

if type_ == "puuvili" and taste == "hapu":
    print("Vitamiinirikas puuvili")
elif type_ == "puuvili":
    print("Tavaline puuvili")
elif type_ == "köögivili" and taste == "magus":
    print("Magus köögivili")
elif type_ == "köögivili" and taste == "hapu":
    print("Hapu köögivili")
elif type_ == "köögivili":
    print("Tavaline köögivili")
else:
    print("Tundmatu toit")

