import datetime
import webbrowser
import time
import os

def alarm():
    print("Time to get up!")
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    time.sleep(214)
    os.system("taskkill /im firefox.exe /f")
    alarm()

hour = int(input("Enter the hour that you want to wake up: "))
minute = int(input("Enter the minute that you want to wake up: "))

timeStamp = datetime.time( hour,minute,0 )


while True:
    if (datetime.datetime.now().time() > timeStamp):
        alarm()
        break;
