from pytube import YouTube
import keyboard
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
browser.get("https://www.youtube.com/")
    
    

def video(data):
    youtube_link = str(data)
    print(youtube_link)
    w = YouTube(youtube_link).streams.first()
    w.download(output_path="C:\\Users\\ADI\\Desktop\\video")
    playsound('done.wav')

def audio(data):
    youtube_link = str(data)
    print(youtube_link)
    y = YouTube(youtube_link)
    t = y.streams.filter(only_audio=True)
    t[0].download(output_path= "C:\\Users\\ADI\\Desktop\\audio")
    playsound('done.wav')





while True:
    while True:
        if keyboard.is_pressed('ctrl + q'):
            try:
                video(browser.current_url)
                break
            except:
                break
                
        elif keyboard.is_pressed('ctrl + y'):
            try:
                audio(browser.current_url)
                break
            except:
                break