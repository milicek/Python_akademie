#uložit jméno
jmeno = "Lukáš"

#uložit příjmení 
prijmeni = "Dvořák"

#uložit celé jméno
cele_jmeno = jmeno + " " + prijmeni

#vypsat celé jméno
print("Celé jméno:", cele_jmeno)

#uložit délku jména
delka_jmena = len(cele_jmeno)

#vypsat délku jména
print("Délka jména:", delka_jmena)

#vypsat delku jmena ohraničené shora i zespoda řadou rovnítek
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)