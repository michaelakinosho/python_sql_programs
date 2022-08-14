# Credit: source of solution is AlgoExpert provided solution
# def caesarCipherEncryptor(string, key):
#     newLetters = []
#     newKey = key % 26
#     for letter in string:
#         newLetters.append(getNewLetter(letter, newKey))
#     return "".join(newLetters)

# def getNewLetter(letter, key):
#     newLetterCode = ord(letter) + key
#     return chr(newLetterCode) if newLetterCode <= 122 else char(96 + newLetterCode % 122)

def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    lower_alphabet = list("abcdefghijklmnopqrstuvwxyz")
    upper_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, lower_alphabet,upper_alphabet))
    return "".join(newLetters)

def getNewLetter(letter, key, lower_alphabet, upper_alphabet):
    if letter in lower_alphabet:
        newLetterCode = lower_alphabet.index(letter) + key
        return lower_alphabet[newLetterCode % 26]
    elif letter in upper_alphabet:
        newLetterCode = upper_alphabet.index(letter) + key
        return upper_alphabet[newLetterCode % 26]

print(caesarCipherEncryptor("xyz", 2))
print(caesarCipherEncryptor("XyZ", 2))