#!/usr/bin/env python
import modules
import sys
import time
from colorama import Fore, Style
from modules.detect import cls

def menu():
    cls()
    print("MAIN MENU \n  1. Add eBay Views \n  2. Supreme Monitor \n  3. Test Proxies \n  0. Exit \n")
    choice = input("Enter Option: ")

    if choice == "1":
        from modules.eBay import add_views
        add_views()
        menu()

    elif choice == "2":
        from modules.supreme import spmonitor
        spmonitor()
        menu()

    elif choice == "3":
        from modules.testProxies import main
        main()
        menu()

    elif choice == "0":
        sys.exit()

    else:
        print(Fore.RED + "INVALID OPTION!")
        print(Style.RESET_ALL)
        time.sleep(.7)
        menu()   

menu()