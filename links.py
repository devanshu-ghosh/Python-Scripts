import requests
def linkGenerate():
    #http://www.juexam.org/newexam/show_result.asp?f1=ITE163018&f2=E3ITE1621R
    for i in range(1,71):
        if i<10:
            path = 'http://www.juexam.org/newexam/show_result.asp?f1=ITE16300'+str(i)+'&f2=E3ITE1621R'
        else:
            path = 'http://www.juexam.org/newexam/show_result.asp?f1=ITE1630'+str(i)+'&f2=E3ITE1621R'
        print(path)
        res = requests.get(path)
        try:
            res.raise_for_status()
        except:
            continue
        file = open('D:\\sem4res\\'+str(i)+'.html','wb')
        for chunk in res.iter_content(100000):
            file.write(chunk)
        print('Okay Done '+str(i))
        file.close()
linkGenerate()
