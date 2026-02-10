import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


# New features

def open_notepad():
    print("Voice Assistant: Opening Notepad.")
    speaker.speak("Opening Notepad.")
    os.system("notepad.exe")


def open_calculator():
    print("Voice Assistant: Opening Calculator.")
    speaker.speak("Opening Calculator.")
    os.system("calc.exe")


def open_file_explorer():
    print("Voice Assistant: Opening File Explorer.")
    speaker.speak("Opening File Explorer.")
    os.system("explorer.exe")


def open_command_prompt():
    print("Voice Assistant: Opening Command Prompt.")
    speaker.speak("Opening Command Prompt.")
    os.system("cmd.exe")


def open_paint():
    print("Voice Assistant: Opening Paint.")
    speaker.speak("Opening Paint.")
    os.system("mspaint.exe")


def open_wordpad():
    print("Voice Assistant: Opening WordPad.")
    speaker.speak("Opening WordPad.")
    os.system("write.exe")


def open_task_manager():
    print("Voice Assistant: Opening Task Manager.")
    speaker.speak("Opening Task Manager.")
    os.system("taskmgr.exe")


def open_settings():
    print("Voice Assistant: Opening Settings.")
    speaker.speak("Opening Settings.")
    os.system("ms-settings:")


def open_control_panel():
    print("Voice Assistant: Opening Control Panel.")
    speaker.speak("Opening Control Panel.")
    os.system("control.exe")


def open_chrome():
    print("Voice Assistant: Opening Google Chrome.")
    speaker.speak("Opening Google Chrome.")
    os.system("chrome.exe")


def open_firefox():
    print("Voice Assistant: Opening Mozilla Firefox.")
    speaker.speak("Opening Mozilla Firefox.")
    os.system("firefox.exe")


def open_edge():
    print("Voice Assistant: Opening Microsoft Edge.")
    speaker.speak("Opening Microsoft Edge.")
    os.system("msedge.exe")


def open_notepadplusplus():
    print("Voice Assistant: Opening Notepad++.")
    speaker.speak("Opening Notepad++.")
    os.system("notepad++.exe")


def open_visual_studio_code():
    print("Voice Assistant: Opening Visual Studio Code.")
    speaker.speak("Opening Visual Studio Code.")
    os.system("code.exe")


def open_excel():
    print("Voice Assistant: Opening Microsoft Excel.")
    speaker.speak("Opening Microsoft Excel.")
    os.system("excel.exe")
