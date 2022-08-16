# Credit: source of solution is AlgoExpert provided solution
# def firstNonRepeatingCharacter(string):
#     for idx in range(len(string)):
#         foundDuplicate = False
#         for idx2 in range(len(string)):
#             if string[idx] == string[idx2] and idx != idx2:
#                 foundDuplicate True
                
#         if not foundDuplicate:
#             return idx
        
#     return -1

def firstNonRepeatingCharacter(string):
    characterFrequencies = {}
    
    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1
        
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
        
    return -1