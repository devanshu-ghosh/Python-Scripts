import os,shutil
##i = 97
##while i!=123:
##    os.makedirs('D:\\GEEKS\\'+chr(i))
##    i = i + 1

os.chdir('D:\\g\\g')
dirlist = os.listdir()
for folder in dirlist:
    charType = ord(folder[0])
    if charType >=98 and charType<=122:
        print(folder)
        print('D:\\GEEKS\\'+chr(charType))
        try:
            shutil.move(folder,'D:\\GEEKS\\'+chr(charType)+'\\'+folder)
        except NotADirectoryError:
            print("ERROR")
