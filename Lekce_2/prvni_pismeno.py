vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = 9

if cislo_dne not in vstupni_cisla :
    print('Špatná vstupní hodnota')
else :
    print('Správná vstupní hodnota')
    den_tydne = tyden[cislo_dne - 1]

    if den_tydne[0] == vstupni_pismena[cislo_dne - 1] :
        print('Správné písmeno')
    else :
        print('Špatné písmeno')

