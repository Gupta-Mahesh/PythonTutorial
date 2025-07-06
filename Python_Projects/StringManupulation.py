


# Create a program that reverses a string without using the built-in [::-1] slicing.
def reverseWords(words):
    temp = ""
    word_count = len(words)-1
    for wd in range(word_count, -1 ,-1):
        temp += words[wd]
    return "The reverse word is : " + str(temp)

#Write a function that checks if a given string is a palindrome (reads the same forwards and backward).
def isPalindone(words):
    temp = ""
    word_count = len(words)-1
    for wd in range(word_count, -1 ,-1):
        temp += words[wd]
    if temp.lower() == words.lower():
        return "The word is palindrome (case insensitive)."
    else:
        return "This is not a palindrome."


user_words = "MOm"


print(reverseWords(user_words))

print(isPalindone(user_words))