def changeWord(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        return word + "way"
    else: 
        return word[1:] + word[0] + "ay"
        
def pigLatin(sentence):
    if len(sentence) == 1:
        return changeWord(sentence[0])
    else:
        return changeWord(sentence[0]) + " " + pigLatin(sentence[1:])
    

sentence = list(map(str, input("Enter sentence: ").split()))
print("Converted: " + pigLatin(sentence))
