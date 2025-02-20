cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0

for cislo in cisla:
    if cislo % 2  > 0:
        licha = licha + cislo
    else:
        suda = suda + cislo

vysledek = licha - suda

print("Rozdíl je: ", abs(vysledek))
