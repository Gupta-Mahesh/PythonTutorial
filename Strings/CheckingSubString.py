
# Checking one string data into another string
# This is possible using "in" function

s1="I am Mahesh and am a true person"
s2="am"

print(s2 in s1)     #It will return the boolean value


# printing the index of value

print(s1.index(s2))
print(s1.rindex(s2))        # checking from right index
print(s1.index(s2,3,len(s1)))    # start and end index