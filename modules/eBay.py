import requests
from os import system
import time
system('clear')
system('cls')

def add_views():
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
    listing_url = input("eBay listing link? ") #ask the user for there listing url
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
