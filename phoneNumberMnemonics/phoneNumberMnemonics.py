# Based on solution provided by AlgoExpert Solution
def phoneNumberMnemonics(phoneNumber):
    currentMnemonic = ["0"] * len(phoneNumber)
    mnemonicsFound = []
    i = 0
    print("\n")
    phoneNumberMnemonicsHelper(0, i, phoneNumber, currentMnemonic, mnemonicsFound)
    return mnemonicsFound

def phoneNumberMnemonicsHelper(idx, i, phoneNumber, currentMnemonic, mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonic = "".join(currentMnemonic)
        mnemonicsFound.append(mnemonic)
    else:
        digit = phoneNumber[idx]
        letters = DIGIT_LETTERS[digit]
        
        for letter in letters:
            print(f"i is: {i}, index is: {idx}  {letter}, {letters}")
            i += 1
            currentMnemonic[idx] = letter
            print(f"currentMnemonic is: {currentMnemonic}\n")
            phoneNumberMnemonicsHelper(idx + 1, i, phoneNumber, currentMnemonic, mnemonicsFound)
        print("\n")

DIGIT_LETTERS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

phoneNumber = "22"
print(phoneNumberMnemonics(phoneNumber))