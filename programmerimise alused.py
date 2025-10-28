# ------------------------
# define list
arr = ["Tere", "nimi", "on", "xd", "kool", "tthk", "auto", 5.5]

# print first and last elements
print("First element:", arr[0])
print("Last element:", arr[-1])
print("First element again:", arr[0])
print("Last element using len:", arr[len(arr)-1])
print("Middle element:", arr[len(arr)//2])

# loop through list and skip index 5
print("Elements of arr (skipping index 5):")
for i in range(len(arr)):
    if i == 5:
        continue
    else:
        print(arr[i])

# slices
firstElements = arr[0:4]
middleToEnd = arr[len(arr)//2:]
middleElement = arr[len(arr)//2]

print("First 4 elements:", firstElements)
print("From middle to end:", middleToEnd)
print("Middle element again:", middleElement)
print("Third from last element:", arr[-3])
print("Last element:", arr[-1])

# append new element
arr.append("uus")
print("After append('uus'):", arr)

# ------------------------
# define another list for numbers
myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

oddArr = []
evenArr = []

# separate odd and even numbers
for n in range(len(myArr)):
    if myArr[n] % 2 == 0:
        evenArr.append(myArr[n])
    else:
        oddArr.append(myArr[n])

print("Odd numbers:", oddArr)
print("Even numbers:", evenArr)

# remove number 5 from myArr if it exists
if 5 in myArr:
    myArr.remove(5)
print("myArr after removing 5:", myArr)

# ------------------------
# define basket list
basket = ["milk", "bread", "eggs"]
print("Initial basket:", basket)

# add 'butter' to last position
basket.append("butter")
print("After append('butter'):", basket)

# add 'tea' to first position
basket.insert(0, "tea")
print("After insert(0, 'tea'):", basket)

# define a new list arr1
arr1 = ["coffee", "milk"]
print("arr1:", arr1)

# reset basket to ["bread", "eggs"] and add 'tea'
basket = ["bread", "eggs"]
basket.append("tea")
print("After append('tea'):", basket)

# combine arr1 with basket
basket = arr1 + basket
print("After combining with arr1:", basket)

# insert 'sugar' at index 2
basket.insert(2, "sugar")
print("After insert(2, 'sugar'):", basket)

# print each element individually and remove items with length > 4
print("Elements of the basket (removing items with length > 4):")
for elem in basket[:]:  # iterate over a copy to safely remove
    if len(elem) > 4:
        basket.remove(elem)
        print(f"After removing '{elem}':", basket)
    else:
        print(elem)

# final basket
print("Final basket:", basket)
