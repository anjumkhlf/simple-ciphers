"""

i invented this in 5th grade instead of talking to people

encode:
    encodes a string
decode:
    decodes a string

no support for punctuation/numbers/spaces (yet)

"""

def fix_num(num):
        return (num + (26 * 3)) % 26
    
def strip_text(text):
    txt = ""
    for letter in text:
        if letter.isalpha():
            txt += letter
    return txt

def encode(text):
    
    """
    
    Encodes a string (removes any spaces, numbers, or punctuation)
    
    """

    from random import randint as rand
    encrypted = ""
    for letter in text:
        if letter != " ":
            letter = letter.lower()
            num = rand(0, 25)
            num2 = fix_num( ord(letter) - 97 - num - 1)
            encrypted += chr(num + 97) 
            encrypted += chr(num2 + 97)

    return encrypted

def decode(text):

    """
    
    Decodes a string (does not support spaced, numbers, or punctutation)
    
    """

    decoded_text = ""

    text2 = strip_text(text)
    text_list = [text2[i:i+2] for i in range(0, len(text2), 2)]

    for item in text_list:
        decoded_text += chr((ord(item[0]) + ord(item[1]) - 192) % 26 + 96)

    return(decoded_text)

