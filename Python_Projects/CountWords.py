
#Write a program that takes a sentence as input and counts the number of words, vowels, and consonants.

words = input("Enter the words which you want count: ")

total_words = len(words)
print("Total words with Spaces: ",total_words)

vawels =0
space = 0
for count in words:
    if count in ["A", "a" , "E", "e", "I", "i","O","o","U","u"]:
        vawels +=1
    if count == " ":
        space +=1
    
print("Spaces : ", space)
print("Vawels : ", vawels)
print("Consonants :" , (total_words - space)-vawels)
print("Total Words Count : ", total_words - space)

