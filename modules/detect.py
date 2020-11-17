from os import system
import platform

def cls():
    os = platform.system()
    if os == "Windows":
        system('cls')
    elif os == "Linux":
        system('clear')