import random
#1,2 a 3. úkol uživatelské vložení jména a příjmení
name = input("jak se jmenujete?")  
surname = input("jaké je vaše příjmení")
print("Jmenujete se:" ,name,surname)
#4 a 9. úkol uživatelské vložení věku (jen čísel)
age= input("Zadejte věk: ")
if age.isdigit():
  print("Děkuji, váš věk je", age)
else:
  print("Zadej jen celočíselnou hodnotu.")
 
#5.úkol délka jména, zadána uživatelem
namelen = (len(name))
surnamelen = (len(surname))
print("délka jména",namelen)
print("délka příjmení",surnamelen)

#6,7 a 8, úkol cyklus, který se 5 zopakuje, a pak se vypíše
promena = 6
x = 0
for x in range (1,6) :
 promena += 3
print ("proměná se rovná:",promena)

#10 náhodné číslo
rn = random.randint(1, 10)
print("náhodné číslo je:".rn)

