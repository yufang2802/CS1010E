def isPalindrome(word):
    if len(word) < 2: 
        return 1
    elif word[0] != word[-1]:
        return 0
    else:
        return isPalindrome(word[1:-1])
         

word = (input("Enter word: ")).lower()

if isPalindrome(word) == 1:
    print("'" + word + "' is a palindrome.")
elif isPalindrome(word) == 0: 
    print("'" + word + "' is not a palindrome." )