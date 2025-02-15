"""

Encodes a string using the ROT-13 cipher. Because encoding is the same as decoding in ROT-13, there is only one function.

encode(text):
    Returns a string encoded with ROT-13

"""

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
