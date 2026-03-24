

# Simple idea

alpha_low = 'abcdefghijklmnopqrstuvwxyz'
alpha_up = alpha_low.upper()

word = 'Surjudprzdqlh13z@'

def caesar(encrypt_or_decrypt, liczba, word):
    if encrypt_or_decrypt == 'encrypt':
        sign = 1
    elif encrypt_or_decrypt == 'decrypt':
        sign = -1
    else:
        return "Podaj właściwa wrtość"
    
    crypted = ''
    for letter in word:
        if letter.islower():
            alpha = alpha_low
        elif letter.isupper():
            alpha = alpha_up
        else:
            crypted += letter
            continue
        
        new_index = (alpha.find(letter) + sign * liczba) % 26
        new_letter = alpha[new_index]
        crypted += new_letter
        
    return crypted