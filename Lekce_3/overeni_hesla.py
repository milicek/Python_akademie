#zápis proměnných
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}

#kontrola zda se shoduje proměnná se slovníkem
if uzivatel.get(jmeno) == heslo:
    print("Ahoj", jmeno, "vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku")