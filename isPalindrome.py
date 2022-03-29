def isPalindrome(string):
    # Write your code here.
    ans = True
    myLen = len(string)
    i = 0
    while i < myLen/2:
        if string[i] != string[myLen-1-i]:
            ans = False
            break
        i += 1
      
    return ans
  
words = "abcdcba"
print(isPalindrome(words))