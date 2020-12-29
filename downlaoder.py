from pytube import YouTube
import keyboard
import win32clipboard
import time
from playsound import playsound


    

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
                keyboard.press_and_release('ctrl + c')
                win32clipboard.OpenClipboard()
                data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                video(data)
                break
            except:
                break
                
        elif keyboard.is_pressed('ctrl + y'):
            try:
                keyboard.press_and_release('ctrl + c')
                win32clipboard.OpenClipboard()
                data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                audio(data)
                break
            except:
                break






