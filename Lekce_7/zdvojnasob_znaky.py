
vstup = 'Ahoj všem'

def zdvojnasob_vsechny_znaky(zadani):
    vystup = ""
    for pismeno in zadani:
        vystup = vystup + (2* pismeno)
    return vystup

vysledek = zdvojnasob_vsechny_znaky(vstup)
print(vysledek)
