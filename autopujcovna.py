class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km): 
            self.registracni_znacka = registracni_znacka
            self.typ_vozidla = typ_vozidla
            self.najete_km = najete_km
            self.dostupne = True

    def pujc_auto(self): 
         if self.dostupne:
              print("Potvrzuji zapujceni vozidla")
              self.dostupne = False
         else:
              print("Vozidlo neni k dispozici.")
             
    def get_info(self):
        return f"Auto {self.typ_vozidla} ma registracni znacku {self.registracni_znacka}."
    
    def vrat_auto(self, stav_tachometru, days):
         self.stav_tachometru = stav_tachometru
         self.days = days
         self.dostupne = True
         if days < 7:
              return f"Cena zapujceni je {days * 400} Kc."
         else:
              return f"Cena zapujceni je {days * 300} Kc."


Auto1 = Auto("4AP 3020", "Peugeot Cabrio 403", 47534)
Auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

uzivatel_preference = input("Jakou znacku auto si prejete pujcit? (Peugeot nebo Škoda)")
if uzivatel_preference == "Peugeot":
    print(Auto1.get_info())
    Auto1.pujc_auto()

elif uzivatel_preference == "Škoda":
    print(Auto2.get_info())
    Auto2.pujc_auto()
else:
     print("Bohuzel, muzete si vybrat pouze Pegueot nebo Škoda")
