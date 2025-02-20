vysledek = list()
start = int(input("start :"))
stop = int(input("stop :"))
delitel = int(input("dělitel :"))

if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int) :
    print("Zadaný rozsah: <", start, ",", stop, ">")
    for cislo in range(start, (stop + 1)) :
        if cislo % delitel == 0 :
            vysledek.append(cislo)
        else:
            continue
    print("Čísla dělitelná", delitel, ": ", vysledek)
else:
    print("Zadané vstupy musí být čísla.")

