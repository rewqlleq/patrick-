# Exercise 1 - Time of Day
time = int(input("Enter the hour (1-24): "))

if time < 7:
    print("It's still night time.")
elif time <= 12:
    print("Good morning!")
elif time <= 18:
    print("Good afternoon!")
else:
    print("Good evening!")

print("\n=============================================\n")


# Exercise 2 - Drink Choice
pref = input("Do you like your drink hot or cold? ")

if pref == "Hot":
    kind = input("Would you like Tea or Coffee? ")
    if kind == "Tea":
        print("Here’s your tea!")
    elif kind == "Coffee":
        print("Here’s your coffee!")
    else:
        print("We’ll get you something hot anyway.")
else:
    print("You’ll get a refreshing lemonade!")

print("\n=============================================\n")


# Exercise 3 - Color Type
color = input("Pick a color: ")

if color == "Red":
    print("That’s a bright color!")
elif color == "Blue":
    print("That’s a calm color.")
else:
    print("That’s a nice color!")

print("\n=============================================\n")


# Exercise 4 - Transport and Weather
transport = input("What transport do you choose? ")
weather = input("How’s the weather? ")

if transport == "Bus":
    if weather == "Rain":
        print("You’re taking the bus through the rain.")
    else:
        print("A nice and comfy bus ride.")
else:
    if weather == "Rain":
        print("Better grab an umbrella for the walk.")
    else:
        print("A pleasant walk ahead!")

print("\n=============================================\n")


# Exercise 5 - Food Type
food = input("Is it a Fruit or a Vegetable? ")
taste = input("Is it Sweet, Sour, or something else? ")

if food == "Fruit" and taste == "Sweet":
    print("That’s a delicious fruit!")
elif food == "Fruit" and taste == "Sour":
    print("That fruit is full of vitamins!")
elif food == "Fruit":
    print("Just a regular fruit.")
elif food == "Vegetable" and taste == "Sweet":
    print("That’s a sweet vegetable!")
elif food == "Vegetable" and taste == "Sour":
    print("That’s a tangy vegetable!")
elif food == "Vegetable":
    print("Just a regular vegetable.")

print("\n=============================================\n")


# Exercise 5 - Alternative
item = input("Fruit or Vegetable? ")
flavor = input("Sweet or Sour? ")
print(flavor + " " + item)
