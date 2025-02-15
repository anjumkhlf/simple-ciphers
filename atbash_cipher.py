"""

Encodes a string using the Atbash cipher. Because encoding is the same as decoding in Atbash, there is only one function.

encode(text):
    Returns a string encoded with Atbash cipher

"""

def encode(text):
    text2 = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                text2 += chr(ord(letter) * -1 + 155)
            else:
                text2 += chr(ord(letter) * -1 + 219)
        else:
            text2 += letter
            
    return text2
