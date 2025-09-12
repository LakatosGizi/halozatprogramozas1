import random

gondolt_szam=random.randint(1,3)

#print (f"A gondolt szám:{gondolt_szam}")
bekert_szam=int(input("kérem a tippet: "))

if gondolt_szam==bekert_szam:
    print("eltalátad!")
elif gondolt_szam > bekert_szam:
    print("nagyobbra gondoltam!")

else:
    print("kisebbre gondoltam")