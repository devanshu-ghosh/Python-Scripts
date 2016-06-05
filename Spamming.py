import random
import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
#browser.get("file:///C:/Users/Devanshu/Downloads/Jadavpur%20University%20-%20Confessions.htm")
fileInput  = open('C:\\Users\\Devanshu\\Desktop\\quotes.txt','r')
d = ['CSE' ,'IT' , 'Power' , 'ECE' ,'Food Tech' , 'Chemical']
#start loop
i = 1
while i<=100:
    browser.get("https://docs.google.com/forms/d/1EzOJyBXUSF2QO4egVW4eng8pGyjfSIN6m1EXjSSJcpg/viewform")
    #browser.get("file:///C:/Users/Devanshu/Downloads/Jadavpur%20University%20-%20Confessions.htm")
    #fill gender
    prevTime = datetime.datetime.now()
    while True:
        currentTime = datetime.datetime.now()
        diff = currentTime - prevTime
        minute = diff/timedelta(minutes=1)
        if minute>0.05:
            break
    gen = 'haha'
    if i%2==0:
        gen = 'group_2083488484_1'
    else:
        gen = 'group_2083488484_2'

    gender = browser.find_element_by_id(gen)
    gender.click()
    #fill dept
    dept = browser.find_element_by_id('entry_646721168')
    dept_name = d[random.randint(0,10)%6]
    dept_name = dept_name + ' 2016'
    dept.send_keys(dept_name)
    #Fill confession
    stuff = browser.find_element_by_id('entry_173103255')
    fill = 'I just have to say this quote : '
    string = fileInput.readline()
    if string=='\n':
        string = fileInput.readline()
    f = string.split('\n');
    fill = fill + f[0]
    stuff.send_keys(fill)
    #HIT submit button
    submit = browser.find_element_by_id('ss-submit')
    submit.click()
    i=i+1
    #wait 3 seconds
    prevTime = datetime.datetime.now()
    while True:
        currentTime = datetime.datetime.now()
        diff = currentTime - prevTime
        minute = diff/timedelta(minutes=1)
        if minute>0.1:
            break
    #wait for the new item on the new page
    #browser.implicitly_wait(7)
    #j=1
    #while j<=10000000:
    #    j = j + 1
    #open new tab
    #body = browser.find_element_by_tag_name('html')
    #body.send_keys(Keys.CONTROL + 'w')
    #close previous tab
    #newpage = browser.find_elements_by_class_name('ss-bottom-link')
    #newpage.click()
    
