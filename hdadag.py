# ===========================================
# A) Tekstimenüü whilega
# ===========================================

text = ""

while True:
    print("\nMenu:")
    print("1. Enter text")
    print("2. Trim spaces (strip)")
    print("3. Remove double spaces (while loop)")
    print("4. Show length without spaces")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        text = input("Enter some text: ")
    
    elif choice == "2":
        if text:
            text = text.strip()
            print("Text after trimming:", text)
        else:
            print("First, enter text.")
    
    elif choice == "3":
        if text:
            while "  " in text:
                text = text.replace("  ", " ")
            print("Text after removing double spaces:", text)
        else:
            print("First, enter text.")
    
    elif choice == "4":
        if text:
            length_without_spaces = len(text.replace(" ", ""))
            print("Length without spaces:", length_without_spaces)
        else:
            print("First, enter text.")
    
    elif choice == "5":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid option, please choose between 1–5.")


print("\n" + "="*60 + "\n")

# ===========================================
# B) Sisselogimisnime kontroll tsüklis
# ===========================================

while True:
    username = input("Enter a username: ")
         
    if len(username) < 4 or len(username) > 12:
        print("Username must be between 4 and 12 characters.")
    elif not username.isalnum():
        print("Username can only contain letters and digits.")
    else:
        print("Username is valid.")
        break  # Exit the loop if valid


print("\n" + "="*60 + "\n")

# ===========================================
# C) Nimesiltide generaator komadega loendist
# ===========================================

name = input("Input text in an F/N or F/N/P format:\n")
name = ' '.join(name.split()).title()
name_parts = name.split()
if len(name_parts) < 2:
    print("Invalid input. Please provide at least two parts.")
else:
    normalized_name = ' '.join(name_parts)
    print("Normalized Name:", normalized_name)

print("\n" + "="*60 + "\n")

# ===========================================
# A) “Sanitizer” stringile
# ===========================================

input_text = input("Enter text to sanitize: ")

input_text = input_text.strip()
input_text = input_text.replace("\t", " ").replace("\n", " ")

sanitized_text = ""
prev_space = False
i = 0

while i < len(input_text):
    char = input_text[i]
    
    if char.isalnum(): 
        sanitized_text += char
        prev_space = False
    elif char == " ":
        if not prev_space: 
            sanitized_text += " "
            prev_space = True
    # Ignore other characters
    i += 1  

print("Sanitized Text:", sanitized_text)

print("\n" + "="*60 + "\n")

# ===========================================
# B) Reasisestuse kokkuvõte (сводка)
# ===========================================

sanitized_text = ""
line_count = 0
word_count = 0
char_count = 0

while True:
    textiga = input("Enter lines (empty line to stop): ")

    if textiga == "":
        break
    
    textiga = textiga.strip()
    textiga = textiga.replace("\t", " ").replace("\n", " ")

    line_clean = ""
    prev_space = False
    for char in textiga:
        if char.isalnum():
            line_clean += char
            prev_space = False
        elif char == " ":
            if not prev_space:
                line_clean += " "
                prev_space = True
        # Ignore punctuation etc.

    sanitized_text += line_clean + "\n"
    line_count += 1
    word_count += len(line_clean.split())
    char_count += len(line_clean.replace(" ", ""))

print("\nCleaned Text:")
print(sanitized_text)

print("Summary:")
print(f"  Lines entered: {line_count}")
print(f"  Total words:   {word_count}")
print(f"  Total letters: {char_count}")
