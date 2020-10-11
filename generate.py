import sys
import random 


if len(sys.argv) != 2:
  kol_vo = int(input("Сколько сгенерировать: "))
else:
  kol_vo = int(sys.argv[1])


f = open("nomber.txt", "w")

a = 0
b = 9
nomber = []
num = "+7+(9"

for i in range(kol_vo):
  n1 = str(random.randint(a,b))
  n2 = str(random.randint(a,b))
  n3 = str(random.randint(a,b))
  n4 = str(random.randint(a,b))
  n5 = str(random.randint(a,b))
  n6 = str(random.randint(a,b))
  n7 = str(random.randint(a,b))
  n8 = str(random.randint(a,b))
  n9 = str(random.randint(a,b))
  nom = num + n1 + n2 + ")+" + n3 + n4 +n5 + "-" + n6+n7+"-" + n8+n9
  nomber.append(nom)

for i in nomber:
   c = i + "\n"
   f.write(c)
f.close()


