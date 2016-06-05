import random
import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get("file:///C:/Users/Devanshu/Downloads/2048-master/2048-master/index.html")
#get tags
control = browser.find_element_by_tag_name('html')
score = browser.find_element_by_class_name('score-container')
restart = browser.find_element_by_class_name('restart-button')
control.click()
count = 0
gameNo = 21
while gameNo <= 40:
    #for every game we create a new list and at the end we write that to a file
    fileOutput = open('D:\\2048\\2048_data'+str(gameNo)+'.txt','w')
    data = ''
    prev_score = 0
    new_score = 0
    steps=0
    while True :
            if count>15:#mechanism to detect game end
                count=0
                break
            else:
                control.click()
                steps = steps + 1
                choice = random.randint(0,4)%4
                data = data + (' ' + str(choice))
                if choice == 0 :
                    control.send_keys(Keys.UP)
                elif choice == 1 :
                    control.send_keys(Keys.DOWN)
                elif choice == 2 :
                    control.send_keys(Keys.LEFT)
                elif choice == 3 :
                    control.send_keys(Keys.RIGHT)
                    
                r = (score.text).split( );
                new_score = int(r[0])
                data = data + (' ' + str(new_score-prev_score))
                
                #check for game_end
                if new_score == prev_score:
                    count = count + 1
                else:
                    count = 0
                    prev_score = new_score

    gameNo = gameNo + 1
    #game has ended , time to save the data
    fileOutput.write(str(steps)+' ')
    fileOutput.write(data)
    restart.click()

fileOutput.close()
