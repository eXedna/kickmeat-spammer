import requests
from time import sleep
import random
from colorama import Fore

a = 40000
b = 111589

f = open("catalog.txt", "a")

phone = "+7+(965)+589-25-69"

for i in range(a,b):
  proxy = {"http" : "http://95.54.196.135:3128"}
  link = "https://www.kickmeat.ru/l-oneclick/" + str(i)
  try:
    c = requests.post(link, {"phone":phone}, proxies = proxy)
    if c.status_code < 300:
      print(Fore.GREEN + str(link) + "                [OK]")
      l = link+"\n"
      f.write(l)
    else:
      print(Fore.RED + str(link) + "                [NO]")
  except IOError as e:
    print("error " + str(e))
f.close()


