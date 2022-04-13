MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def cripto(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvxwyz'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

# Teste
key = 13
original = 'xuxu'
print('Original:', original)
ciphered = cripto(original, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = cripto(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain)
