import math

#Funkce, ktera overi platnost cisla, pokud je jeho delka 9 nebo 13, tak vrati True

def delka_cisla (telefonni_cislo):
    delka = len(telefonni_cislo)
    if delka == 9:
        return True
    elif delka == 13:
        return True
    else:
        return False
telefonni_cislo = str(input('Zadejte telefonni cislo: '))

#Funkce, ktera počítá cenu zprávy - každých 180 znaků stojí 3 Kč.
def cena_zpravy (text_zpravy):
    pocet_zprav = (len(str(text_zpravy))/180)
    cena = math.ceil(pocet_zprav) * 3
    return cena
    print(cena)

if delka_cisla(telefonni_cislo) == True:
    text_Vasi_zpravy = str(input('Zadejte Vasi zpravu:'))
    print(f'Cena Vasi zpravy je {cena_zpravy(text_Vasi_zpravy)} Kc.')
else:
    print('Zadejte spravne telefonni cislo.')
 

