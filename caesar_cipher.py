def encode(text, key):
    text2 = ""

    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                text2 += chr(((ord(letter) - 65) + key) % 26 + 65)
            else:
                text2 += chr(((ord(letter) - 97) + key) % 26 + 97)
        else:
            text2 += letter
        
    return text2

def decode(text, key):
    text2 = ""

    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                text2 += chr(((ord(letter) - 65) - key + 26) % 26 + 65)
            else:
                text2 += chr(((ord(letter) - 97) - key + 26) % 26 + 97)
        else:
            text2 += letter

    return text2