import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#open the browser
browser = webdriver.Firefox()
browser.get("file:///C:/Users/Devanshu/Downloads/2048-master/2048-master/index.html")
#browser.get("https://gabrielecirulli.github.io/2048/")
#get tags
control = browser.find_element_by_tag_name('html')
score = browser.find_element_by_class_name('score-container')
#end = browser.find_element_by_class_name('mailing_list_form')
control.click()
count = 0
prev_score = '0'
while True :
    if count>15:
        break
    else:
        control.click()
        choice = random.randint(0,4)
        if choice == 0 :
            control.send_keys(Keys.UP)
        elif choice == 1 :
            control.send_keys(Keys.DOWN)
        elif choice == 2 :
            control.send_keys(Keys.LEFT)
        elif choice == 3 :
            control.send_keys(Keys.RIGHT)
        r = (score.text).split( );
        print(r[0])
        if r[0]==prev_score:
            count = count + 1
            prev_score = r[0]
        else:
            count = 0
            prev_score = r[0]
