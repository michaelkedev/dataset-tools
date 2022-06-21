from os import listdir
import os
import time
def generateName():
    global count
    newName = "%05d" % count +"."+a
    while os.path.isfile(newName):
        count+=1
        print(newName)
        newName = "%05d" % count +"."+a
        print(f"exist, new name {newName}")
    return newName
def startFrom1():
    count = 1
    files = listdir("./")
    for i in files:
        oldName = i
        newName=""
        if a in i:
            newName = "%05d" % count +"."+a
            # newName = generateName()
            # print(newName)
            # os.rename(f'{oldName}', f'{newName}')
            count+=1
path = "./"
os.chdir(path)
print(path)
files = listdir("./")
a = input("txt/jpg?")
print(f"You choice is {a}")
if os.path.exists("./classes.txt"):
    print("Removing classes.txt")
    os.remove("./classes.txt")
files = listdir("./")
print("Start!")
count = int(input("Start from?"))
print(f"Start form {count}")
for i in files:
    # print("Starting ...")
    oldName = i
    newName=""
    if a in i:
        # newName = "%05d" % count +"."+a
        newName = generateName()
        print(newName)
        os.rename(f'{oldName}', f'{newName}')
startFrom1()