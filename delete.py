import os

imagePath = "./Image/"
labelPath = "./Label/"

imageFile = os.listdir(imagePath)
for i in range(5):
    print(imageFile[i])

labelFile = os.listdir(labelPath)
for i in range(5):
    print(labelFile[i])
while 1:
    fileName = int(input("You want to delete ? "))
    filejpgName = "%05d" % fileName+".jpg"
    print(filejpgName)
    filelableName = "%05d" % fileName+".txt"
    print(filelableName)

    try:
        #刪除檔案
        os.remove(f"{imagePath}{filejpgName}")
        #確認檔案刪除
        if os.path.exists(f"{imagePath}{filejpgName}"):
            print("1. Remove failed")
        else:
            print("1. Remove.")

        #刪除檔案
        os.remove(f"{labelPath}{filelableName}")
        #確認檔案刪除
        if os.path.exists(f"{labelPath}{filelableName}"):
            print("2. Remove failed")
        else:
            print("2. Remove.")
    except:
        pass