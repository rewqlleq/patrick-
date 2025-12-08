# Task solutions without functions

# 1 Arithmetic
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
op = input("Tehe (+ - * /): ")
if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/": print(a / b)
else: print("Tundmatu tehe")

# 2 Leap year
year = int(input("Aasta: "))
print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

# 3 Square
a = float(input("Ruudu külg: "))
perim = 4 * a
area = a * a
diag = a * (2 ** 0.5)
print(perim, area, diag)

# 4 Season
month = int(input("Kuu number: "))
if month in (12,1,2): print("talv")
elif month in (3,4,5): print("kevad")
elif month in (6,7,8): print("suvi")
elif month in (9,10,11): print("sügis")
else: print("vigane kuu")

# 5 Bank deposit
a = float(input("Summa: "))
years = int(input("Aastad: "))
for i in range(years): a *= 1.10
print(a)

# 6 Prime check
n = int(input("Arv: "))
if n < 2:
    print(False)
else:
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Kordarv, jagajad:", i, "ja", n//i)
            prime = False
            break
    print(prime)

# 7 Valid date
day = int(input("Päev: "))
month = int(input("Kuu: "))
year = int(input("Aasta: "))
import datetime
try:
    datetime.date(year,month,day)
    print(True)
except ValueError:
    print(False)

# 8 XOR cipher
text = input("Tekst: ")
key = input("Võti: ")
cipher = "".join(chr(ord(c)^ord(key)) for c in text)
print("Krüpteeritud:", cipher)
uncipher = "".join(chr(ord(c)^ord(key)) for c in cipher)
print("Dekrüpteeritud:", uncipher)

# 9 Average
nums = input("Sisesta numbrid: ").split()
nums = [float(x) for x in nums]
print(None if len(nums)==0 else sum(nums)/len(nums))

# 10 Min max
nums = input("Sisesta numbrid: ").split()
nums = [float(x) for x in nums]
print(min(nums), max(nums))

# 11 Unique elements
lst = input("Sisesta elemendid: ").split()
res=[]
for x in lst:
    if x not in res:
        res.append(x)
print(res)
