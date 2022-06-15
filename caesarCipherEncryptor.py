from string import ascii_lowercase


def caesarCipherEncryptor(string, key):
    myletters = ascii_lowercase
    idx = myletters.find(string)
    myStr = ""
    if idx < key:
        myStr = myletters[25-key:]
    else:
        myStr = myletters[idx-key:idx+key-1]
    print(myStr)
caesarCipherEncryptor("abc",18)
caesarCipherEncryptor("hij",2)