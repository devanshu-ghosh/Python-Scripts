#What it does is that it keeps on writing clipboard content to
#file every 0.01 min and if and only if the content is not same
#The end word is github.txt which can be easily changed to mean something else


import pyperclip,datetime
from datetime import timedelta

prevTime = datetime.datetime.now()
prev_copied = pyperclip.paste()
while True:
    copied = pyperclip.paste()
    if copied.find('github.txt')!=(-1):
        break
    
    currentTime = datetime.datetime.now()
    diff = currentTime - prevTime
    minute = diff/timedelta(minutes=1)
    
    if  minute>0.01 and prev_copied!=copied:
            fileOutput = open('D:\\GEEKS\\clipboard.txt','a')
            fileOutput.write('\n\n'+currentTime.isoformat()+'\n\n')
            fileOutput.write(copied)
            fileOutput.close()
            prevTime = datetime.datetime.now()
            prev_copied = copied
