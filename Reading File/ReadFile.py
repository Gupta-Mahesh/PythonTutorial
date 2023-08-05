
inline =open("D:\\Python Practice\\Reading File\\test.txt","r")
print(inline.read())
inline.close()

inline1 =open("D:\\Python Practice\\Reading File\\Inventory.txt","r")
print(inline1.read())
inline1.close()

inline =open("D:\\Python Practice\\Reading File\\test1.txt","w")
inline.writelines("Hi beta")
inline.close