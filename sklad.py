sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadejte kod soucastky: ")

if kod in sklad:
    pocet = int(input("Zadejte potrebne mnozstvi: "))
    if pocet > sklad[kod]:
        print(f'Zadane mnozstvi neni na sklade, mame pouze {sklad[kod]} kusu.')
        pocet_kusu = sklad.pop(kod)
        print(sklad)
    else:
        print("Dekujeme, Vasi poptavku lze uspokojitv plne vysi.")
        sklad[kod] = sklad[kod] - pocet
        print(f'Na sklade zbyva {sklad[kod]} kusu.')
else:
    print("Tato soucastka bohuzel neni na sklade.")