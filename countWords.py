import string

def countWords(sentence):
    # totalWords = 0
    # for i in sentence:
    #     if str(i.split(string.punctuation)).isalpha() == True:
    #         totalWords += 1
    # return totalWords
    totalWords = sum([i.strip(string.punctuation).isalpha() for i in sentence.split()])
    return totalWords

print("Enter a sentence with at most 50 characters:")
sentence = input("Sentence = ")

print("Word count = " + str(countWords(sentence)))