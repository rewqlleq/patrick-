# Ülesanne 1: päevaaja määramine tunni järgi
def paevatund(hour: int) -> str:
    if 0 <= hour < 6:
        return "Öö"
    elif 6 <= hour < 12:
        return "Hommik"
    elif 12 <= hour < 18:
        return "Päev"
    elif 18 <= hour < 24:
        return "Õhtu"
    else:
        return "Vale tund"


# Ülesanne 2: joogi valik eelistuse järgi
def jook(preference: str) -> str:
    if preference.lower() == "kuum":
        return "Kohv"
    elif preference.lower() == "külm":
        return "Limonaad"
    else:
        return "Tundmatu eelistus"


# Ülesanne 3: riietuse värvi kontroll
def riide_varv(color: str) -> str:
    if color.lower() == "punane":
        return "Ere"
    elif color.lower() == "sinine":
        return "Rahulik"
    else:
        return "Tavaline"


# Ülesanne 4: marsruudi valik transpordi ja ilma järgi
def marsruut(transport: str, weather: str) -> str:
    transport = transport.lower()
    weather = weather.lower()

    if transport == "buss" and weather == "vihm":
        return "Sõidame bussiga katuse all"
    elif transport == "buss" and weather == "päike":
        return "Sõidame bussiga mugavalt"
    elif transport == "jalgsi" and weather == "vihm":
        return "Võtame vihmavarju"
    elif transport == "jalgsi" and weather == "päike":
        return "Kõnnime rõõmsalt"
    else:
        return "Tundmatu valik"


# Ülesanne 5: toidu klassifitseerimine tüübi ja maitse järgi
def toit(type_: str, taste: str) -> str:
    type_ = type_.lower()
    taste = taste.lower()

    if type_ == "puuvili":
        if taste == "hapu":
            return "Vitamiinirikas puuvili"
        else:
            return "Tavaline puuvili"
    elif type_ == "köögivili":
        if taste == "magus":
            return "Magus köögivili"
        elif taste == "hapu":
            return "Hapu köögivili"
        else:
            return "Tavaline köögivili"
    else:
        return "Tundmatu toit"


# --- Testime ---
if __name__ == "__main__":
    print("Ülesanne 1:", paevatund(7))       # Hommik
    print("Ülesanne 2:", jook("kuum"))       # Kohv
    print("Ülesanne 3:", riide_varv("sinine")) # Rahulik
    print("Ülesanne 4:", marsruut("buss", "vihm")) # Sõidame bussiga katuse all
    print("Ülesanne 5:", toit("puuvili", "hapu"))  # Vitamiinirikas puuvili
