import requests
from os import system
import time
from .detect import cls
from colorama import Fore, Style

def add_views():
  cls()
  print("------------------------------------------------")
  print("|                                              |")
  print("|             eBay View Bot V1.0.6             |")
  print("|  Let's add some views to your eBay listing!  |")
  print("|                                              |")
  print("------------------------------------------------")
  print("")

  x = True
  count = 0
  while x:
    listing_url = input("eBay listing link? (Press enter to exit): ") #ask the user for there listing url
    if (len(listing_url) == 0):
      print(Fore.YELLOW + "Going back to main menu!")
      x = False
      time.sleep(2)
    elif (listing_url.startswith('http://www.ebay.com') or listing_url.startswith('https://www.ebay.com')):
        view_number = int(input("How many views would you like to add? ")) #ask the user how many views they would like to send?
        for _ in range (int(view_number)):
          count=count+1
          r = requests.get(listing_url) #sends requests to there listing url in a loop for how many times they specified
          print("Successfully sent view ",count)
        print("Successfuly sent", view_number, "views to",listing_url)
        another_listing = input("Would you like to send views to another lisitng? (y/n) ").lower()
        if another_listing == 'y':
          pass
        elif another_listing == 'n':
          x = False
    else:
      print(Fore.RED + "ERROR: Link MUST start with either http://www.ebay.com OR https://www.ebay.com")