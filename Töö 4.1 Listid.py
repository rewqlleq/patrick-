# -------------------------------------------
# 1. Word or sentence analysis
# -------------------------------------------

print("1. Word or sentence analysis")
text = input("Enter word or sentence: ")
lower = text.lower()

vowels = "aeiouy"
cons = "bcdfghjklmnpqrstvwxyz"

vowel_count = 0
cons_count = 0
spaces = 0
symbols = 0

for ch in lower:
    if ch in vowels:
        vowel_count += 1
    elif ch in cons:
        cons_count += 1
    elif ch == " ":
        spaces += 1
    else:
        symbols += 1

print("Vowels:", vowel_count)
print("Consonants:", cons_count)
print("Spaces:", spaces)
print("Other symbols:", symbols)

# -------------------------------------------
# 2. Names
# -------------------------------------------

print("\n2. Names")
names = []
for i in range(5):
    names.append(input("Enter name " + str(i+1) + ": "))

print("Alphabet order:", sorted(names))
print("Last added:", names[-1])

ans = input("Change a name? yes/no: ")
if ans == "yes":
    old = input("Which name to replace?: ")
    new = input("New name: ")
    if old in names:
        names[names.index(old)] = new
    print("Updated list:", names)

# -------------------------------------------
# 2.2 Remove duplicates
# -------------------------------------------

print("\n2.2 Remove duplicates")
names2 = ["Anna","Anna","Mati","Mati","Kati"]
unique = []
for n in names2:
    if n not in unique:
        unique.append(n)
print(unique)

# -------------------------------------------
# 2.3 Ages
# -------------------------------------------

print("\n2.3 Ages")
ages = [12,5,44,18,22,30]
print("Max:", max(ages))
print("Min:", min(ages))
print("Sum:", sum(ages))
print("Average:", sum(ages)/len(ages))

# -------------------------------------------
# 3. Stars diagram
# -------------------------------------------

print("\n3. Stars diagram")
nums = [10,11,16,17,20,12]
for n in nums:
    print("*" * n)

# -------------------------------------------
# 4. Post index
# -------------------------------------------

print("\n4. Post index")
post = input("Enter post index: ")

if post[0] in "123":
    print("Go to sea!")
else:
    print("Go to forest!")

# -------------------------------------------
# 5. Swap pairs
# -------------------------------------------

print("\n5. Swap pairs")
arr = [1,2,3,4,5,6,7,8]
print("Original:", arr)

k = int(input("How many pairs to swap?: "))

for i in range(k):
    arr[i], arr[-1-i] = arr[-1-i], arr[i]

print("After swap:", arr)

# -------------------------------------------
# 6. Replace max with max/len
# -------------------------------------------

print("\n6. Replace max")
lst = [3,15,8,1,9]
m = max(lst)
lst[lst.index(m)] = m / len(lst)
print(lst)

# -------------------------------------------
# 7. Sort by absolute value
# -------------------------------------------

print("\n7. Sort by absolute value")
nums2 = [-5,3,-10,1,8]
mode = input("Ascending? a / Descending? d : ")
if mode == "a":
    print(sorted(nums2, key=lambda x: abs(x)))
else:
    print(sorted(nums2, key=lambda x: abs(x), reverse=True))

# -------------------------------------------
# 8. Make all strings same length
# -------------------------------------------

print("\n8. Equal length strings")

lists = [
    ["tamm","taevas","elevant"],
    ["a","aa","aaa","aaaa","aaaaa"],
    ["qweasdqweas","q","rteww","ewqqqqq"]
]

for lst in lists:
    m = max(len(x) for x in lst)
    for i in range(len(lst)):
        lst[i] = lst[i] + "_" * (m - len(lst[i]))
    print(lst)

# -------------------------------------------
# 9. Name check
# -------------------------------------------

print("\n9. Name check")
name = input("Enter name: ")

if name.isalpha():
    print("Hello,", name.capitalize())
else:
    print("Invalid name!")

v = 0
c = 0
for ch in name.lower():
    if ch in vowels:
        v += 1
    elif ch in cons:
        c += 1

print("Vowels:", v)
print("Consonants:", c)
print("Sorted letters:", sorted(set(name.lower())))

# -------------------------------------------
# 10. Workers
# -------------------------------------------

print("\n10. Workers data")
workers = [
    ["Mari",1200,25],
    ["Jyri",900,33],
    ["Anna",1500,30],
    ["Karl",800,28]
]

max_worker = max(workers, key=lambda x: x[1])
print("Highest salary:", max_worker)

avg_salary = sum(w[1] for w in workers)/len(workers)
print("Average salary:", avg_salary)

above = [w for w in workers if w[1] > avg_salary]
print("Count above average:", len(above))

below_age = [w[2] for w in workers if w[1] <= avg_salary]
above_age = [w[2] for w in workers if w[1] > avg_salary]

print("Avg age <= average salary:", sum(below_age)/len(below_age))
print("Avg age > average salary:", sum(above_age)/len(above_age))

# -------------------------------------------
# 11. Alphabet lists
# -------------------------------------------

print("\n11. Alphabet lists")

import string
alpha = list(string.ascii_lowercase)
print(alpha)

alpha2 = []
for i, ch in enumerate(alpha):
    alpha2.append(ch * (i+1))
print(alpha2)

# -------------------------------------------
# 12. Swap min/max
# -------------------------------------------

print("\n12. Swap min and max")
import random
arr = [random.randint(1,50) for _ in range(10)]
print("Original:", arr)

mn = min(arr)
mx = max(arr)
i1 = arr.index(mn)
i2 = arr.index(mx)
arr[i1], arr[i2] = arr[i2], arr[i1]

print("After:", arr)

# -------------------------------------------
# 13. Guess the word
# -------------------------------------------

print("\n13. Guess the word")
word = random.choice(["auto","cat","sun","home"])
hidden = ["_"] * len(word)
wrong = []
tries = 0

while "_" in hidden:
    print("Word:", " ".join(hidden))
    letter = input("Enter letter: ")
    tries += 1

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
    else:
        wrong.append(letter)

print("Correct word:", word)
print("Wrong letters:", wrong)
print("Attempts:", tries)

# -------------------------------------------
# 14. Capital cities
# -------------------------------------------

print("\n14. Capital cities")

cities = ["Madrid","Paris","Rome","Berlin","Oslo","Lisbon","Vienna","Tallinn","Helsinki","Prague"]

for c in cities:
    print(c)

cities.sort()
print("Sorted:", cities)

for i in range(2):
    cities.append(input("Add new capital: "))

cities.sort()

for i, c in enumerate(cities, start=1):
    print(i, c)

print("Total capitals:", len(cities))

# -------------------------------------------
# 15. Dictionary lists
# -------------------------------------------

print("\n15. Simple dictionary")

nums = ["1","2","3","4"]
est = ["uks","kaks","kolm","neli"]
eng = ["one","two","three","four"]
ita = ["uno","due","tre","quattro"]

# add 2 new
nums += ["5","6"]
est += ["viis","kuus"]
eng += ["five","six"]
ita += ["cinque","sei"]

for i in range(len(nums)):
    print(nums[i], est[i], eng[i], ita[i])

print("Is 'tre' in italian list?", "tre" in ita)

print("Sorted nums:", sorted(nums))
print("Sorted est:", sorted(est))
print("Sorted eng:", sorted(eng))
print("Sorted ita:", sorted(ita))

# -------------------------------------------
# 16. Yes/No answer
# -------------------------------------------

print("\n16. Yes/No answers")
answ = ["Yes, sure!", "Yes!", "Maybe!", "No!"]
q = input("Ask question: ")
print(random.choice(answ))
