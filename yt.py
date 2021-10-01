import time
import pyautogui
import webbrowser
import random

number = input("number of views:-")
sleep_time = random.randint(25, 30)

webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open('')
time.sleep(5)

for i in range(number):
	pyautogui.hotkey('ctrl', 'r')
	print("Watching for {} time".format(i))
	time.sleep(sleep_time) 
