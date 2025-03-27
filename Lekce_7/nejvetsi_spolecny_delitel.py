
def najdi_gcd(x1:int, x2:int) -> int:
    modulo = x1 % x2
    print(modulo)
    vysledek = "Zadal jsi stejná čísla"
    if modulo != x1:
        while True:
            vysledek = x2 % (modulo)
            print(x1, vysledek)
            pomoc = x1 % vysledek
            if pomoc == 0:
                break
    else:
        vysledek = x1
    return vysledek

            
        
        
 

prvni_cislo = 16
druhe_cislo = 16

print(najdi_gcd(prvni_cislo, druhe_cislo))

