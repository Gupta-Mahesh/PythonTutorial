import os

print("Current Dir: ",os.getcwd())

cur_pid = os.getpid()

print("Process ID: ",cur_pid)


#print(os.getcwd())                                               #used to get the current working directory(cwd).

list_dir=os.listdir()
print("List of Dir: ",list_dir)
#os.mkdir
if "test" in list_dir:
    print("Folder already exist")
else:
    print("New folder is created",os.mkdir("test"))                                    #To create a directory in the cwd.

os.chdir("test")                                        #To go inside a folder.

print("Current Dir: ",os.getcwd())

os.chdir("..")                                          #To go back to the previous directory.

print("Current Dir: ",os.getcwd())

if "filename" in os.listdir():
    print("Folders are already exist")
else:
    os.makedirs("filename/filename1/filename2")             #Used to create directories within directories.
    print("Folders are created")


#os.remove("filename/filename1/filename2")                                  #can be used to remove a folder but if folder is empty if it contains anything it can’t be used.

os.rmdir("filename/filename1/filename2")

os.rename("filename","filename2")                      #used to rename a file

os.getsize("filename2")                                 #gives size of folder in kbs.

print("List of dir: ",os.listdir())

import os
print(os.path.exists("test"))
print(os.listdir())