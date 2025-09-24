# Ülesanne 1: päevaaja määramine tunni järgi
def paevatund():
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


# Ülesanne 2: joogi valik eelistuse järgi
def jook():
    preference = input('Sisesta joogi eelistus ("kuum" või "külm"): ').lower()
    if preference == "kuum":
        print("Kohv")
    elif preference == "külm":
        print("Limonaad")
    else:
        print("Tundmatu eelistus")


# Ülesanne 3: riietuse värvi kontroll
def riide_varv():
    color = input('Sisesta värv ("punane", "sinine" või muu): ').lower()
    if color == "punane":
        print("Ere")
    elif color == "sinine":
        print("Rahulik")
    else:
        print("Tavaline")


# Ülesanne 4: marsruudi valik transpordi ja ilma järgi
def marsruut():
    transport = input('Sisesta transport ("buss" või "jalgsi"): ').lower()
    weather = input('Sisesta ilm ("vihm" või "päike"): ').lower()

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


# Ülesanne 5: toidu klassifitseerimine tüübi ja maitse järgi
def toit():
    type_ = input('Sisesta tüüp ("puuvili" või "köögivili"): ').lower()
    taste = input('Sisesta maitse ("magus", "hapu" või muu): ').lower()

    if type_ == "puuvili":
        if taste == "hapu":
            print("Vitamiinirikas puuvili")
        else:
            print("Tavaline puuvili")
    elif type_ == "köögivili":
        if taste == "magus":
            print("Magus köögivili")
        elif taste == "hapu":
            print("Hapu köögivili")
        else:
            print("Tavaline köögivili")
    else:
        print("Tundmatu toit")


# --- Peaprogramm ---
if __name__ == "__main__":
    print("Ülesanne 1")
    paevatund()

    print("\nÜlesanne 2")
    jook()

    print("\nÜlesanne 3")
    riide_varv()

    print("\nÜlesanne 4")
    marsruut()

    print("\nÜlesanne 5")
    toit()
