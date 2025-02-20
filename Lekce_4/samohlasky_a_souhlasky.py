veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledek = dict()
vysledek["samohlasky"] = 0
vysledek["souhlasky"]  = 0

for znak in veta.lower():
    if samohlasky.count(znak)  > 0 :
        vysledek["samohlasky"] = (vysledek['samohlasky'] + 1)
    elif souhlasky.count(znak) > 0 :
        vysledek['souhlasky'] = (vysledek['souhlasky'] + 1)
    else :
        continue

print("počet souhlásek: ", vysledek['souhlasky'] ," | Počet samohlásek: ", vysledek['samohlasky'])
