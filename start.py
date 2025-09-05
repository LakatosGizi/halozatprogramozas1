#feladat : négyzet/téglalap kerűletének számitása
def beker(alakzat, oldal):
    """"bekéri az 'alakzat' 'oldal' oldalának hosszát"""
    oldalhossz =int(input(f"kérem a {alakzat} {oldal} oldalának hosszát[cm]:"))
    return oldalhossz
def teglalapkerulete(a,b):
    """"kiszámolja az "a" és "b" oldal ismeretében a téglalap kerűletét. K/2*(a+b)"""
    kerulet=2*(a+b)
    return kerulet
def kiir(alakzat,kerulet):
    """ki irja az 'alakzat' 'kerulet'-ét"""
    print(f"a {alakzat} kerűlete: {kerulet}cm")
#input
mit=input("[T]églalap vagy [N]égyzet kerűletét számoljam? [T|N]")
if mit.upper()=="N":
    alap =beker("négyzet","a")

    #calculation
    kerulet=teglalapkerulete(alap,alap)

    #output
    kiir("négyzet", kerulet)

elif mit.upper()== "T":
    a_oldal =beker("téglalap","a")
    b_oldal =beker("téglalap","b")

    #calculation
    kerulet=teglalapkerulete(a_oldal,b_oldal)

    #output
    kiir("téglalap",kerulet)
else:
    print("hibás választás kilépek")