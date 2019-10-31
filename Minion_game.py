def minion_game(string):
    # your code goes here

    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0

    for i in range(len(s)):
        if string[i] in vowels:
            kevin_score += (len(s) - i)
        else:
            stuart_score += (len(s) - i)

    #print("Kevin's list:",kevin_set)
    #print("Stuart's list:",stuart_set)
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score == stuart_score:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
