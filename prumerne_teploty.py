teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
] # Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

# Vytvoř seznam průměrných teplot pro každý den.
prumerne_teploty_pres_den = [((teplota[0] + teplota[1] + teplota[2] + teplota[3])/4) for teplota in teploty]
print(prumerne_teploty_pres_den)

# Vytvoř seznam ranních teplot.
ranni_teploty = [teplota[0] for teplota in teploty]
print(ranni_teploty)

# Vytvoř seznam nočních teplot.
nocni_teploty = [teplota[3] for teplota in teploty]
print(nocni_teploty)

# Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledni_a_nocni_teploty = [[teplota[1], teplota [3]] for teplota in teploty]
print(poledni_a_nocni_teploty)

##Muj bonus prumernych teplot (nejdrive jsem omylem pochopila prvni ukol takto, tak kdyz uz to mam, vkladam :))
prumerne_ranni_teploty = sum(teplota[0] for teplota in teploty)/7
prumerne_poledni_teploty = sum(teplota[1] for teplota in teploty)/7
prumerne_odpoledni_teploty = sum(teplota[2] for teplota in teploty)/7
prumerne_nocni_teploty = sum(teplota[3] for teplota in teploty)/7
prumerne_teploty = [prumerne_ranni_teploty, prumerne_poledni_teploty, prumerne_odpoledni_teploty, prumerne_nocni_teploty]
print(prumerne_teploty)

# BONUS
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]
#Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.

prumerne_teploty_pres_den_slovnik = {teplota[0]:((teplota[4] + teplota[1] + teplota[2] + teplota[3])/4) for teplota in teploty}
print(prumerne_teploty_pres_den_slovnik)