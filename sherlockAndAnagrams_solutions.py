import string

q = int(input())

ALPHABET = string.ascii_lowercase

for _ in range(q):
    s = input()
    signatures = {}

    #signature = [0 for _ in ALPHABET]
    #for letter in s:
        #print(ord(letter))
        #print(ord(ALPHABET[0]))
        #print(ord(letter)-ord(ALPHABET[0]))
        #signature[ord(letter)-ord(ALPHABET[0])] += 1
    #print(signature)
    #print("\n")

    # iterate over all substrings of s
    for start in range(len(s)):
        for finish in range(start, len(s)):
            # initialize substring signature
            signature = [0 for _ in ALPHABET]
            #print(signature)
            #print(s[start:finish+1])
            for letter in s[start:finish+1]:
                signature[ord(letter)-ord(ALPHABET[0])] += 1
            # tuples are hashable in contrast to lists
            signature = tuple(signature)
            #print(signature)
            #print(signatures.get(signature,0)+1)
            signatures[signature] = signatures.get(signature,0) + 1
            for t in signatures.items():
                #print(t)
                pass
            #print(signatures)
            #print("\n")

    #print(signatures.values())
    res = 0
    for count in signatures.values():
        #print(count*(count-1)/2)
        res += count*(count-1)/2
    print(int(res))
