letters = 'abcdefghijklmnopqrstuvwxyz'
key =3
def encrypt(plaintext):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >=26:
                    new_index -=26
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext):
    plaintext = ''
    for letter in ciphertext:
        
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1: 
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index +=26
                plaintext += letters[new_index]
    return plaintext

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text)
    print(f'CIPHERTEXT: {ciphertext}')

if user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text)
    print(f'PLAINTEXT: {plaintext}')







