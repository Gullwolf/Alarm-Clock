#George O Cook - AlarmClock.py
import datetime
from datetime import timedelta
import webbrowser
import time
import os
from sys import platform
import json
import urllib.request
import re

def alarm(): #Function that carried out the alarm, opens a web browser and then sleeps till the alarm has ended then closes the webpage.
    print("Time to get up!")
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    time.sleep(214)
    if (platform == "linux" or platform == "linux2"):
        os.system("pkill firefox")

    elif platform == "darwin":
        browser = webbrowser.get('macosx')
        os.system("killall -9 '"+browser+"'")

    elif platform == "win32":
        #browser = webbrowser.get('windows-default')
        #print("taskkill /im "+browser+" /f")
        os.system("taskkill /im firefox.exe /f")

def alarmClock(sleep): #Function that sleeps the script for the calculated time until wake up.   
    time.sleep(sleep)
    alarm()

def workOutTime(hour, minute): #Function that worksout how long the script needs to sleep for, so the alarm goes off at the required time.
    timeStamp = timedelta(hours=hour, minutes=minute, seconds=0)
    print(timeStamp)
    timeNow = datetime.datetime.now().time()
    timeNow = timedelta(hours=timeNow.hour, minutes=timeNow.minute, seconds=timeNow.second)
    print(timeNow)
    sleep = (timeStamp - timeNow).total_seconds()
    if(sleep < 0):
        sleep = (86400-((timeStamp - timeNow).total_seconds()*-1) )
    print(sleep)
    alarmClock(sleep)

def main(): #main funtion that starts the alarm clock.
    hour = int(input("Enter the hour that you want to wake up: "))
    minute = int(input("Enter the minute that you want to wake up: "))


    video_id="dQw4w9WgXcQ"
    api_key="AIzaSyAjd2SykyTSp3F5fxNUs6thuuB3lURlixA"
    searchUrl="https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=contentDetails"
    response = urllib.request.urlopen(searchUrl).read()
    data = json.loads(response)
    all_data=data['items']
    contentDetails=all_data[0]['contentDetails']
    duration=contentDetails['duration']
    print (duration)

    duration = duration.replace('PT', '')
    duration = duration.replace('S', '')


    
    workOutTime(hour,minute)


main()
