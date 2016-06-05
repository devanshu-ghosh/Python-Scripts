import pyautogui
from PIL import Image
i = 1000
while i>=0 :
    im=pyautogui.screenshot()
    url = 'D:\\GEEKS\\screen\\' + str(i) + '.jpg'
    im.save(url)
    i = i - 1
