#!/usr/bin/env python
# Configuration Settings:
#
# os = Where you want to enter your operating system type. win for windows and linux for Linux.
# gpu = If you have an Nvidia GPU and would like to run on the GPU (FASTER) instead of you CPU enter yes, otherwise enter no.
# proxyList = Enter you list of proxies you want to use separated with a comma. Both IP:PORT and IP:PORT@USER:PASS work. Ex: 127.0.0.1:1, 127.0.0.1:2, 127.0.0.1:3@test.com:password.
# proxyDelay = Delay in seconds between each proxy test. 5 is the default.
#
########################################################### USER EDIT SETTINGS #############################################################
os = "win"
proxyList = ['192.138.2.1:351',
             'username:password@domain:port']
proxyDelay = 5
####################################################### DO NOT EDIT BELOW!!!!!! #######################################################

import sys
from os import system
    
import time
import requests
from os import system
from bs4 import BeautifulSoup
from dhooks import Webhook, Embed
from fake_headers import Headers
from colorama import Fore, Style
import urllib.request
import socket
import urllib.error
import logging
import requests
import requests.auth
import datetime
elapsed_seconds = ''
from flask import Flask, render_template, Response
from .detect import cls
headers = Headers(os="mac", headers=True).generate() # os is the operating system you want the header to be

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        start = datetime.datetime.now()
        req=urllib.request.Request(proxyTestURL)
        sock=urllib.request.urlopen(req)
        end = datetime.datetime.now()
        delta = end - start
        global elapsed_seconds
        elapsed_seconds = round(delta.microseconds * .000001, 6)
    except urllib.error.HTTPError as e:
        print(Fore.RED + 'Error code:', e.code)
        print(Style.RESET_ALL)
        return e.code
    except Exception as detail:
        print(Fore.RED + "ERROR:", detail)
        print(Style.RESET_ALL)
        return True
    return False

def main():
    cls()
    print("------------------------------------------------")
    print("|                                              |")
    print("|             Proxy Tester V1.0.0              |")
    print("|  Test your proxies against a specific site.  |")
    print("|                                              |")
    print("------------------------------------------------")
    print("")
    hostnameInput = input("Enter domain name. EX: target.com: ")
    global proxyTestURL
    proxyTestURL = "http://www." + hostnameInput
    print(Fore.YELLOW + "Testing proxies against", proxyTestURL)
    socket.setdefaulttimeout(proxyDelay)
    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print(Fore.RED + "Blocked or Bad Proxy: %s" % (currentProxy))
            print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + "%s PASSED!" % (currentProxy))
            print("Response Time: ", elapsed_seconds)
            print(Style.RESET_ALL)
    time.sleep(5)
