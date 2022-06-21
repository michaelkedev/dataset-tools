import os
from os import listdir

#你的資料夾位置
path = "./construction"
fileName = listdir(path)
print(fileName)
# wantChangeClass = str(input("想要修改的Class?"))
# resultClass = str(input("想要修改成多少?"))
# firstClass = str(input("Class ?"))
for i in fileName:
    if "txt" in i:
        newContext=""
        with open (f'{path}/{i}') as f:
            temp = f.readlines()
            
            for eachLine in temp:
                eachLineSpiltBySpace = eachLine.split()
                print(eachLineSpiltBySpace)
                # if eachLineSpiltBySpace[0] == wantChangeClass:
                #     eachLineSpiltBySpace[0]=resultClass
                # # eachLineSpiltBySpace[0]=firstClass
                # for k in eachLineSpiltBySpace:
                #     newContext+=k+" "
                # # print(eachLineSpiltBySpace)
                # newContext+="\n"
            # print("//////////")
            f.close()
        # with open (f'{path}/{i}', 'w') as f :
        #     f.write(newContext)
        # print(newContext)