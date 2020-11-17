import requests
import time
from os import system
from bs4 import BeautifulSoup
from dhooks import Webhook, Embed
from fake_headers import Headers
from colorama import Fore, Style
import logging
import threading
import sys
system('clear')
system('cls')
headers = Headers(os="mac", headers=True).generate() # os is the operating system you want the header to be
Delay = 5 # Delay between each requests that you send to monitor the site
hook = Webhook("https://discord.com/api/webhooks/776816919298572299/xuWHtHVcDXsY-g8WOGFEkErI4QmnfKb2bkiKWH5M3xy-Cy8ZEufQmR8rGsTcSGGO0Mjj")

def spmonitor():
    print("------------------------------------------------")
    print("|                                              |")
    print("|            Supreme Monitor V1.0.0            |")
    print("|  Let's monitor an item until it is in stock  |")
    print("|                                              |")
    print("------------------------------------------------")
    print("")

    url = input("Enter link to monitor: ")
    print("Monitoring...")
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    x = True

    while x:
        try:
            if soup.find('input',{'class':'button'}):
                print(Fore.GREEN + "IN STOCK")
                print(Style.RESET_ALL)
                price_x = soup.find('p', class_='price').text
                name_x = soup.find('h2', class_='protect').text
                #size-x = soup.find('', ).text
                #picture = soup.find(id='img-main')

                #film_id = 'img-main'
                raw_picture = soup.find(itemprop="image")
                picture_x = 'https:' + (raw_picture["src"])
                print(picture_x)
                x = False
                embed = Embed(title='Restock', description='', color=0x5CDBF0, timestamp='now')
                embed.set_author(name='Supreme Monitor')
                embed.set_image(picture_x)
                embed.add_field(name="Product", value=name_x)
                embed.add_field(name="Price", value=price_x)
                embed.add_field(name="Link", value=url)
                embed.set_footer(text='BOO!')
                hook.send(embed=embed)
                time.sleep(Delay)
        except:
            print("Error finding product or out of stock.")
            time.sleep(Delay)
            x = False

def webhook():
    if sys.version_info[0]==2:
        import six
        from six.moves.urllib import request
        opener = request.build_opener(
            request.ProxyHandler(
                {'http': 'http://username:password@host:port',
                'https': 'http://username:password@host:port'}))
        print(opener.open('http://lumtest.com/myip.json').read())
        time.sleep(10)
    if sys.version_info[0]==3:
        import urllib.request
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {'http': 'http://username:password@host:port',
                'https': 'http://username:password@host:port'}))
        url = input("Enter link to monitor: ")
        print("Monitoring...")
        response = requests.get(url, headers=headers).text
        soup = BeautifulSoup(response, 'lxml')
        x = True

        while x:
            try:
                if soup.find('input',{'class':'button'}):
                    print(Fore.GREEN + "IN STOCK") # Printss test in color
                    print(Style.RESET_ALL) # Clears colors set by fore
                    price_x = soup.find('p', class_='price').text
                    name_x = soup.find('h2', class_='protect').text
                    raw_picture = soup.find(itemprop="image")
                    picture_x = 'https:' + (raw_picture["src"])
                    print("Sending webhook")
                    x = False
                    embed = Embed(title='Restock', description='', color=0x5CDBF0, timestamp='now')
                    embed.set_author(name='Supreme Monitor')
                    embed.set_image(picture_x)
                    embed.add_field(name="Product", value=name_x)
                    embed.add_field(name="Price", value=price_x)
                    embed.add_field(name="Link", value=url)
                    embed.set_footer(text='BOO!')
                    hook.send(embed=embed)
                    time.sleep(Delay)
            except:
                print("Error finding product or out of stock.")
                time.sleep(Delay)
                x = False
            time.sleep(10)

class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False