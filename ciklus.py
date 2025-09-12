#ciklusok

lista=[1,2,3,4,5]

def osszegez(lista):
    osszeg=0
    for elem in lista:
        osszeg+=elem
    return osszeg
print(f"a lista elemeinek összege:{osszegez(lista)}")

def paros_szam(lista):
    osszeg=0
    for elem in lista:
        if elem%2==0:
            darab+=1
    return darab
print(f"A lista páros elemeinek darabszáma:{paros_szam(lista)}")