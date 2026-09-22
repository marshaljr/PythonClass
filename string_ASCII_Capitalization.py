text = input("enter a string: ")

if len(text) <8 :
    print("Please enter a string with at least 8 characters")
else:
    result = ''
    for i in range(len(text)):
        if i % 2 == 0:
            ascii_value = ord(text[i])
            if 97 <= ascii_value <= 122:
                ascii_value = ascii_value - 32
            new_character = chr(ascii_value)
            result = result + new_character
        else:
            result = result + text[i]
            # print(ascii_value)
print(result)


