Okay, here is the text you gave me, but rewritten to sound more human and follow all of your instructions.

```python
# ===========================================
# A) Text Menu with While Loop
# ===========================================

text = 

while True:
    print(\nMenu:)
    print(1. Give me some text)
    print(2. Clean up the edges(strip))
    print(3. Delete extra spaces (while loop))
    print(4. How long is it without spaces?)
    print(5. All done)
    
    choice = input(Pick a number (1-5): )
    
    if choice == 1:
        text = input(Okay, type away: )
    
    elif choice == 2:
        if text:
            text = text.strip()
            print(After cleaning edges:, text)
        else:
            print(Gotta type something first.)
    
    elif choice == 3:
        if text:
            while    in text:
                text = text.replace(  ,  )
            print(No more extra spaces:, text)
        else:
            print(Gotta type something first.)
    
    elif choice == 4:
        if text:
            length_without_spaces = len(text.replace( , ))
            print(Just letters and numbers:, length_without_spaces)
        else:
            print(Gotta type something first.)
    
    elif choice == 5:
        print(Bye!)
        break
    
    else:
        print(Please pick 1, 2, 3, 4, or 5.)


print(\n + =*60 + \n)

# ===========================================
# B) Check the Login Name
# ===========================================

while True:
    username = input(Pick a login name: )
         
    if len(username) &lt; 4 or len(username) &gt; 12:
        print(Needs to be between 4 and 12 letters/numbers.)
    elif not username.isalnum():
        print(Only letters and numbers, please.)
    else:
        print(Looks good!)
        break  # Exit if it's okay


print(\n + =*60 + \n)

# ===========================================
# C) Make Name Tags from a List
# ===========================================

# Here's a name to use
name = ivan ivanov petrovich

# Fix it up: no extra spaces, capital letters
name = ' '.join(name.split()).title()
name_parts = name.split()

if len(name_parts) &lt; 2:
    print(Need at least a first and last name.)
else:
    fixed_name = ' '.join(name_parts)
    print(Fixed Name:, fixed_name)

print(\n + =*60 + \n)

# ===========================================
# A) String Sanitizer
# ===========================================

input_text = input(Type something to clean: )

input_text = input_text.strip()
input_text = input_text.replace(\t,  ).replace(\n,  )

clean_text = 
space_already = False
i = 0

while i &lt; len(input_text):
    char = input_text[i]
    
    if char.isalnum(): 
        clean_text += char
        space_already = False
    elif char ==  :
        if not space_already: 
            clean_text +=  
            space_already = True
    i += 1  

print(Cleaned Up:, clean_text)

print(\n + =*60 + \n)

# ===========================================
# B) Input Summary
# ===========================================

clean_text = 
line_number = 0
word_number = 0
letter_number = 0

while True:
    textiga = input(Type some lines (just hit enter to stop): )

    if textiga == :
        break
    
    textiga = textiga.strip()
    textiga = textiga.replace(\t,  ).replace(\n,  )

    line_clean = 
    space_already = False
    for char in textiga:
        if char.isalnum():
            line_clean += char
            space_already = False
        elif char ==  :
            if not space_already:
                line_clean +=  
                space_already = True

    clean_text += line_clean + \n
    line_number += 1
    word_number += len(line_clean.split())
    letter_number += len(line_clean.replace( , ))

print(\nCleaned Up Text:)
print(clean_text)

print(Here's the Scoop:)
print(f  Lines given: {line_number})
print(f  Total words:   {word_number})
print(f  Just letters: {letter_number})
```
