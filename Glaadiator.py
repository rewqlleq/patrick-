import random

# ===============================================================
#                 GLADIAATOR: SURMARENE! (GLADIATOR: DEATH ARENA)
# ===============================================================

print("======================================================================")
print("                 TERE TULEMAST SURMARENDELE! (WELCOME TO THE DEATH ARENA!)")
print("======================================================================\n")

# --- VÕITLEJAD (FIGHTERS) ---
nimed = ["SPARTAKUS", "KRIKS", "FLAMMA", "COMMODUS"]
elu = [100, 120, 90, 110]
vastupidavus = [60, 40, 70, 50]
kirjeldus = [
    "Legendaarne ülestõusujuht, mõõga ja kilbi meister (Legendary rebel leader, master of sword and shield)",
    "Raevukas gallialane kahekäemõõgaga (Furious Gaul warrior with a greatsword)",
    "Kiire ja surmav kolmikoda ja võrk (Fast and deadly with trident and net)",
    "Rooma keiser, kes januneb verd areenil (Roman emperor thirsting for blood)"
]

# --- Mängija valik (PLAYER CHOICE) ---
print("Vali oma võitleja (Choose your fighter):\n")
for i in range(len(nimed)):
    print(f"{i+1} - {nimed[i]} ({elu[i]} elu (HP), {vastupidavus[i]} vastupidavust (Stamina))")
    print(f"   {kirjeldus[i]}")
print()

mangija_valik = int(input("Sinu valik (Your choice 1-4): ")) - 1
print(f"\nSa valisid {nimed[mangija_valik]}! (You chose {nimed[mangija_valik]})\n")

# --- Vastase valik (CHOOSE OPPONENT) ---
print("Nüüd vali oma vastane (Now choose your opponent):")
for i in range(len(nimed)):
    if i != mangija_valik:
        print(f"{i+1} - {nimed[i]}")
vastane_valik = int(input("Vastase valik (Opponent choice 1-4): ")) - 1

while vastane_valik == mangija_valik:
    print("Sa ei saa võidelda iseendaga! (You cannot fight yourself!)")
    vastane_valik = int(input("Vastase valik (Opponent choice 1-4): ")) - 1

print("\n======================================================================")
print(f"{nimed[mangija_valik]} vs {nimed[vastane_valik]}!")
print("Jumalad himustavad vaatemängu! (The gods crave spectacle!) Alustagem võitlust! (Let the fight begin!)")
print("======================================================================\n")

# --- Algväärtused (INITIAL VALUES) ---
m_hp = elu[mangija_valik]
m_sta = vastupidavus[mangija_valik]
v_hp = elu[vastane_valik]
v_sta = vastupidavus[vastane_valik]
max_m_hp = m_hp
max_v_hp = v_hp
max_m_sta = m_sta
max_v_sta = v_sta

ring = 1

# --- Põhivõitlus (MAIN FIGHT LOOP) ---
while m_hp > 0 and v_hp > 0:
    print(f"\n[RING {ring}]")
    print("------------------------------------------------------------------")
    print(f"Sinu elud (Your HP): {m_hp}/{max_m_hp} | Vastupidavus (Stamina): {m_sta}/{max_m_sta}")
    print(f"{nimed[vastane_valik]} elud (HP): {v_hp}/{max_v_hp} | Vastupidavus (Stamina): {v_sta}/{max_v_sta}")
    print("------------------------------------------------------------------")
    print("Vali tegevus (Choose your action):")
    print("1 - Ründa tugevalt (Strong Attack, costs 15 stamina)")
    print("2 - Taktikaline löök (Quick Attack, costs 10 stamina)")
    print("3 - Kaitse (Defend, costs 5 stamina)")
    print("4 - Puhka (Rest, restores 20 stamina)")
    tegu = int(input("Sinu käik (Your move): "))

    # --- Mängija tegevus (PLAYER ACTION) ---
    mangija_kahju = 0
    kaitse = False

    if tegu == 1 and m_sta >= 15:
        mangija_kahju = random.randint(15, 25)
        m_sta -= 15
        print(f"{nimed[mangija_valik]} annab purustava hoobi (delivers a crushing blow) ja teeb {mangija_kahju} kahju (damage)!")
    elif tegu == 2 and m_sta >= 10:
        mangija_kahju = random.randint(10, 18)
        m_sta -= 10
        print(f"{nimed[mangija_valik]} teeb kiire löögi (makes a quick strike) ja põhjustab {mangija_kahju} kahju (damage)!")
    elif tegu == 3 and m_sta >= 5:
        kaitse = True
        m_sta -= 5
        print(f"{nimed[mangija_valik]} tõstab kilbi (raises the shield) ja valmistub kaitseks (prepares for defense)!")
    elif tegu == 4:
        taast = 20
        m_sta += taast
        if m_sta > max_m_sta:
            m_sta = max_m_sta
        print(f"{nimed[mangija_valik]} puhkas (rested) ja taastab {taast} vastupidavust (stamina)!")
    else:
        print("Sa oled liiga väsinud selle tegevuse jaoks! (You are too tired for that!)")

    # --- Vastase tegevus (ENEMY ACTION) ---
    vastase_tegu = random.randint(1, 4)
    vastase_kahju = 0
    v_kaitse = False

    if vastase_tegu == 1 and v_sta >= 15:
        vastase_kahju = random.randint(15, 22)
        v_sta -= 15
        print(f"{nimed[vastane_valik]} ründab tugevalt (strikes hard) ja teeb {vastase_kahju} kahju (damage)!")
    elif vastase_tegu == 2 and v_sta >= 10:
        vastase_kahju = random.randint(8, 16)
        v_sta -= 10
        print(f"{nimed[vastane_valik]} lööb kiirelt (attacks swiftly) ja teeb {vastase_kahju} kahju (damage)!")
    elif vastase_tegu == 3 and v_sta >= 5:
        v_kaitse = True
        v_sta -= 5
        print(f"{nimed[vastane_valik]} kaitseb end (defends)!")
    elif vastase_tegu == 4:
        taast = 20
        v_sta += taast
        if v_sta > max_v_sta:
            v_sta = max_v_sta
        print(f"{nimed[vastane_valik]} taastub (recovers) ja kogub jõudu (regains strength)!")
    else:
        print(f"{nimed[vastane_valik]} on liiga väsinud (too tired to act)!")

    # --- Kahju arvutamine (DAMAGE CALCULATION) ---
    if v_kaitse:
        mangija_kahju = int(mangija_kahju * 0.5)
    if kaitse:
        vastase_kahju = int(vastase_kahju * 0.5)

    v_hp -= mangija_kahju
    m_hp -= vastase_kahju

    if mangija_kahju > 0:
        print(f"{nimed[vastane_valik]} kaotab {mangija_kahju} elupunkti (loses HP)!")
    if vastase_kahju > 0:
        print(f"{nimed[mangija_valik]} kaotab {vastase_kahju} elupunkti (loses HP)!")

    if v_hp <= 0 or m_hp <= 0:
        break

    ring += 1

# --- Mängu lõpp (END GAME) ---
print("\n======================================================================")
if m_hp <= 0 and v_hp <= 0:
    print("Mõlemad kukuvad verisele liivale... Viik! (Both fall to the sand... Draw!)")
elif m_hp <= 0:
    print(f"{nimed[vastane_valik]} VÕIDAB! (WINS!) Veri voolab areenile! (Blood flows on the sand!)")
else:
    print(f"{nimed[mangija_valik]} VÕIDAB! (WINS!) Rahvas juubeldab! (The crowd cheers!)")
print("======================================================================\n")

print("Mäng läbi. Aitäh, et võitlesid au ja vabaduse nimel! (Game over. Thank you for fighting for glory and freedom!)")
