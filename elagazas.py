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

#készits fűggvényt elöjel néven mely átvesz egy egész számot és az elöjelét adja vissza
def elojel(szam):
    if szam>0:
        return"+"
    else:
        return"-"
szam=int(input("kérek egy számot elöjellel: "))
print(f"A{szam}elojele: {elojel(szam)}.")
print(f"a {szam}elojele: {'+' if szam>0 else '-'}")
def tesztesetek():
    teszt(5,"+")
    teszt(-3,"-")
    teszt(-1,"-")
    teszt(0,"+")
    teszt(1,"+")
def teszt(szam,elvart_elojel):
    if elojel(szam)==elvart_elojel:
        print(f"elojel({szam})=={elvart_elojel}ture")
    else:
        print(f"elojel({szam})=={elvart_elojel}false")
tesztesetek()