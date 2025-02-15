def encode(text):
    text2 = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                text2 += chr(ord(letter) % 26 + 65)
            else:
                text2 += chr((ord(letter) - 6) % 26 + 97)
        else:
            text2 += letter
            
    return text2