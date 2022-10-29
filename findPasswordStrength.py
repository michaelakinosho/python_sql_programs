def findPasswordStrength(password):
    vowels = ['a','e','i','o','u']
    
    passwordStrength = 0
    passwordList = [n for n in password]
    trackConsonantsVowels = [0,0]
    
    for char in password:
        if char not in vowels and trackConsonantsVowels[0] == 0:
            trackConsonantsVowels[0] = 1
        elif char in vowels and trackConsonantsVowels[1] == 0:
            trackConsonantsVowels[1] = 1
                    
        if sum(trackConsonantsVowels) == 2:
            passwordStrength += 1
            trackConsonantsVowels = [0,0]

    return passwordStrength
    
    
print(findPasswordStrength("hackerrank"))