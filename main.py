'''
uzduotis = "5 + 3"
atsakymas = 5 + 3

with open("krituliaiviso.txt", "w", encoding="utf-8") as failas:
    failas.write(f"Užduotis: {uzduotis}\n")
    failas.write(f"Atsakymas: {atsakymas}\n")
'''
'''
with open("krituliai.txt", "r", encoding="utf-8") as failas:
    uzduotis = failas.read().split()

    atsakymas = int(uzduotis[0]) + int(uzduotis[2])

with open("krituliaiviso.txt", "w", encoding="utf-8") as failas:
    failas.write(str(atsakymas))

'''

'''
atsakymai = []

with open("krituliai.txt", "r", encoding="utf-8") as failas:
    for eilute in failas:
        dalys = eilute.split()
        if not dalys:
            continue

        if dalys[0].endswith("."):
            numeris = dalys[0]
            skaiciai = dalys[1:]
            atsakymai.append(f"{numeris} {sum(map(int, skaiciai))}")

        else:
            atsakymai.append(str(sum(map(int, dalys))))

with open("krituliaiviso.txt", "w", encoding="utf-8") as failas:
    failas.write("\n".join(atsakymai))
    
'''

'''
atsakymai = []

with open("krituliai.txt", "r", encoding="utf-8") as failas:
    for eilute in failas:
        dalys = eilute.split()
        if not dalys:
            continue

        
        numeris = dalys[0]
        pirmas = int(dalys[1])
        antras = int(dalys[2])

        rezultatas = pirmas - antras

        atsakymai.append(f"{numeris} {rezultatas}")

with open("krituliaiviso.txt", "w", encoding="utf-8") as failas:
    failas.write("\n".join(atsakymai))

'''      

darbo_laikas = 8
pelno_dalis_procentais = 0.15
kepalai_per_valanda = int(input("Iveskite kiek kepalų gali iškepti per vieną valandą vienas darbuotojas: "))
print()
darb_sk = int(input("Iveskite kiek kepykla turi darbuotaju: "))
print()

valiuta = "Eur."

kepalo_savikaina = float(input("Įveskite vieno kepalo savikaina: "))
print()
kepalo_pard_kaina = float(input("Įveskite kainą už kurią parduodą kepalus: "))
print()

uzsakymai  = int(input("Kiek turi parduoti kepalų? "))
print()


kiekis = darbo_laikas * kepalai_per_valanda * darb_sk

if kiekis > uzsakymai:
    bendra_savikaina = kiekis * kepalo_savikaina
    pajamos = kiekis * kepalo_pard_kaina

    pelnas = pajamos - bendra_savikaina

    pelno_dalis = pelnas * pelno_dalis_procentais

    print("Kepykla užsidirbo", pelno_dalis, valiuta)
    print()

else:
    print("nespės")




