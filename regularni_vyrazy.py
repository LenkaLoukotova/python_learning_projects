import re 
"""
Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:
platná data:
2.2.2022
13. 8. 1999
4/5/2001
neplatná data:
5.123.458.91
21.4
8./9
"""
regularni_vyraz1 = re.compile(r"\d+[./].?\d+[./].?\d{4}")

"""
Zkopíruj si obsah souboru posta.txt do regex101 jako testovací řetězec. Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu. Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 nebo 742 45 FULNEK. Celkem by jich mělo být 18.
"""
regularni_vyraz2 = re.compile(r"\d{3} \d{2}  ?\w* ?\w* ?\w*")

"""Napiš program, který se zeptá uživatele na jeho přihlašovací jméno, e-mailovou adresu a heslo. Po každém zadaném údaji program ověří jeho správnost podle následujících pravidel:
uživatelské jméno smí obsahovat malá a velká písmena (nesmí obsahovat žádné jiné znaky), jeho minimálná délka je 6 znaků a jeho maximální délka je 10 znaků.
heslo smí obsahovat malá a velká písmena, číslice, a následující speciální znaky: _, -, ., +, =. Jeho minimálná délka je 12 znaků a jeho maximální délka je 30 znaků.
e-mail by měl být validním e-mailem"""

regularni_vyraz_jmeno = re.compile(r"[a-zA-Z]{6,10}")
regularni_vyraz_heslo = re.compile(r"[a-zA-Z0-9_+.=-]{12,30}")
regularni_vyraz_email = re.compile(r"[a-zA-Z0-9_+.=\-\"\[\]]{1,100}@[a-zA-Z0-9_+.=\-\"\[\]]{1,100}\.\w+.?\w*.?\w*")

jmeno = input("Zadejte sve uzivatelske jmeno:")
jmeno_ok = regularni_vyraz_jmeno.fullmatch(jmeno)

if jmeno_ok:
    heslo = input("Zadejte sve heslo:")
    heslo_ok = regularni_vyraz_heslo.fullmatch(heslo)
    if heslo_ok:
        email = input("Zadejte svuj email:")
        email_ok = regularni_vyraz_email.fullmatch(email)
        if email_ok:
            print("Dekujeme, Vami zadane udaje jsou v poradku.")
        else:
            print("Nespravny email.")
    else:
        print("Nespravne heslo")
else:
    print("Nespravne uzivatelske jmeno")


