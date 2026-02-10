from pyautogui import click, write
import keyboard
from time import sleep


def Whatsapp_msg(name, msg):
    sleep(3)

    # Search contact
    click(x=271, y=137)
    sleep(1)
    write(name)

    # Click on contact
    sleep(2)
    click(x=248, y=233)
    sleep(2)

    # Click message box
    click(x=837, y=964)
    sleep(1)

    # Send message
    write(msg)
    sleep(1)
    keyboard.press("enter")

    sleep(3)

    # Close WhatsApp
    click(x=1890, y=2)
    sleep(5)


def Whatsapp_call(name):
    sleep(3)

    # Search contact
    click(x=271, y=137)
    sleep(1)
    write(name)

    # Click on contact
    sleep(2)
    click(x=248, y=233)
    sleep(2)

    # Call button
    click(x=1781, y=82)

    # Wait until Ctrl key is pressed to end call
    keyboard.wait("ctrl")
    click(x=1085, y=830)

    sleep(3)

    # Close WhatsApp
    click(x=1890, y=2)
    sleep(5)


def Whatsapp_video_call(name):
    sleep(3)

    # Search contact
    click(x=271, y=137)
    sleep(1)
    write(name)

    # Click on contact
    sleep(2)
    click(x=248, y=233)
    sleep(2)

    # Video call button
    click(x=1729, y=91)

    # Wait until Ctrl key is pressed to end call
    keyboard.wait("ctrl")
    click(x=1103, y=936)

    sleep(3)

    # Close WhatsApp
    click(x=1890, y=2)
    sleep(5)
