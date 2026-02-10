import win32com.client
import speech_recognition as sr
import webbrowser
import datetime
import winsound
import time
import Whats_app
import chat_app
import news_app
import weather_app
import pyautogui
import keyboard
from translate import Translator
from alarm import set_alarm
from word2number import w2n
import snake
import pyqrcode
import turtle
import os
from youtube import play_specified_song, watch_specified_movie, play_specified_video
from joke import tell_joke, get_riddle, check_answer
from volume import set_system_volume, change_volume
import open_files
import random
import parsedatetime
import remainder
import system_info
from location import get_user_location
import schedule
from dateutil import parser
import re
import threading

# speaker setup
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        try:
            audio = r.listen(source, timeout=20)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user: {query}")
            return query

        except sr.WaitTimeoutError:
            print("Voice Assistant: Timeout. No speech detected.")
            return "Timeout. No speech detected."

        except sr.UnknownValueError:
            print("Voice Assistant: Sorry, I could not understand that.")
            return "Sorry, I could not understand that."

        except sr.RequestError as e:
            print(f"Voice Assistant: Could not request results; {e}")
            return "Could not request results from Google Speech Recognition service."


def schedule_video_play(video_name, hour, minute):
    current_time = time.localtime()
    alarm_time = time.struct_time((
        current_time.tm_year,
        current_time.tm_mon,
        current_time.tm_mday,
        int(hour),
        int(minute),
        0, 0, 0, 0
    ))

    if alarm_time > current_time:
        time_difference = time.mktime(alarm_time) - time.mktime(current_time)
        print(f"Video will play at {hour}:{minute}")

        def play_video():
            print(f"Voice Assistant: Playing '{video_name}' on YouTube at {hour}:{minute}.")
            speaker.speak(f"Playing {video_name} on YouTube")
            play_specified_video(video_name)

        threading.Timer(time_difference, play_video).start()
    else:
        print("Invalid time. Please provide a future time.")


def volume_up():
    change_volume("up")
    print("Voice Assistant: Volume increased.")
    speaker.speak("Volume increased.")


def volume_down():
    change_volume("down")
    print("Voice Assistant: Volume decreased.")
    speaker.speak("Volume decreased.")


def set_volume():
    speaker.speak("Set the volume level between 0 and 100.")
    volume_level = take_command()
    try:
        volume_level = float(volume_level) / 100.0
        set_system_volume(volume_level)
        speaker.speak(f"Volume set to {int(volume_level * 100)} percent.")
    except ValueError:
        speaker.speak("Please provide a valid volume level.")


def shutdown():
    speaker.speak("Shutting down the computer.")
    os.system("shutdown /s /t 1")


def restart():
    speaker.speak("Restarting the computer.")
    os.system("shutdown /r /t 1")


def log_off():
    speaker.speak("Logging off the computer.")
    os.system("shutdown -l")


def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_filename = f"screenshot_{timestamp}.png"
    os.system(f"import -window root {screenshot_filename}")
    speaker.speak(f"Screenshot saved as {screenshot_filename}")


# startup sound
winsound.PlaySound(
    r"C:\Users\M.Sreedhar\OneDrive\Desktop\Team Project\harry.wav",
    winsound.SND_ASYNC
)

print("Say the Secret Code to Start ECHO VOICE ASSISTANT")
speaker.speak("Say the secret code to start ECHO voice assistant")

code = take_command()

if code.lower() == "hello maths":
    speaker.speak("Hello sir, I am MAX AI. How can I help you?")

    while True:
        time.sleep(1)
        speaker.speak("Listening your command")
        query = take_command().lower()

        if "who invented you" in query:
            speaker.speak("I was invented by Sumedha and her team members")

        elif "how are you":
