
#Concatination using + symbol
s1 = "Hi!"
s2="mahesh"
print(s1+s2)
# or
print ("Hi "+ "Mahesh")
# or
s3= "Hello "+"'Kumar'"
print(s3)


#Length 
print ("The length of s3 is ", len(s3))

#upper
print("The s3 value convert to Upper: ", s3.upper())

#lower
print("The s3 value convert to lower: ", s3.lower())

#title
print("First letter of words convert to Upper: ", s3.title())

#isLower or isUpper

print(s2.islower())
print(s1.isupper())

print(s1.startswith("H"))
print(s2.startswith("M"))
print(s1.endswith("lo"))

### split function

s1 = "your are great"

print("Split Function by space: ",s1.split())   # split by space ' '

s2 = "your, are, great"
print("Split Function by comma: ",s2.split(','))        # split by comma ','

l = ["youraregreat","python","learning"]


print("join by space: ", " ".join(l))          # join by space

print("join by comma: ", ", ".join(l))         # join by comma


### Strip

s1 = "__youraregreat__"
print(s1.strip("_"))   # strip from both side
print(s1.lstrip('_'))  # strip from left side
print(s1.rstrip("_"))   # strip from right side

s1 = "--youraregreat--"
print(s1.strip("-"))


### Find

s1 = "your are great"
s2 = "are"
print(s1.find(s2))
print(s1.find("tft"))   #return -1 bcoz string not avlbl
n = len(s1)
print(s1.find(s2,1,n))