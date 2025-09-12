#ciklusok

lista=[1,2,3,4,5]

def osszegez(lista):
    osszeg=0
    for elem in lista:
        osszeg+=elem
    return osszeg
print(f"a lista elemeinek összege:{osszegez(lista)}")

def paros_db(lista):
    darab=0
    for elem in lista:
        if elem % 2 == 0:
            darab += 1
    return darab
print(f"A lista páros elemeinek darabszáma:{paros_db(lista)}")

print("*"*5)
for i in range(5):
    print("*", end="")
print()

magassag = 5

for i in range(1, magassag + 1):
    sor = ' ' * (magassag - i) + '*' * (2 * i - 1)
    print(sor)

n=9
space_db=n-1
csillag_db=1
for i in range(n):
    print(" "* space_db,end="")
    print("*"* csillag_db)
    space_db-=1
    csillag_db+=2

for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:>4}",end="")
    print()