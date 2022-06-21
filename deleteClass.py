import os
from os import listdir

#把不想要的類別刪除
def delClass(targetClass):
    outputDir = "./result/"
    if not os.path.isdir(outputDir):
        print("Create Dir")
        os.mkdir(outputDir)
    path="./"
    fileName=listdir(path)
    for i in fileName:
        if "txt" in i:
            newContent=""
            with open (f'{path}/{i}') as f:
                temp = f.readlines()
                for eachLine in temp:
                    eachLineSpiltBySpace = eachLine.split()
                    # print(eachLineSpiltBySpace)
                    if eachLineSpiltBySpace:
                        if eachLineSpiltBySpace[0] != targetClass:
                            eachLineSpiltBySpace=[]
                    # eachLineSpiltBySpace[0]=firstClass
                    for k in eachLineSpiltBySpace:
                        newContent+=k+" "
                    # print(eachLineSpiltBySpace)
                    newContent+="\n"
                # print("//////////")
                f.close()
            with open (f'{path}/{i}', 'w') as f :
                f.write(newContent)
            print(newContent)
        outputFileName = outputDir+i
        if "txt" in i:
            delblankline(i, outputFileName)
    print("Output to"+outputDir)
    print("Done")
#清除空白行
def delblankline(infile, outfile):
 infopen = open(infile, 'r',encoding="utf-8")
 outfopen = open(outfile, 'w',encoding="utf-8")
 
 lines = infopen.readlines()
 for line in lines:
  if line.split():
   outfopen.writelines(line)
  else:
   outfopen.writelines("")
 
 infopen.close()
 outfopen.close()


classId = input("想要保存的Class? ex:0 \n")
delClass(classId)


