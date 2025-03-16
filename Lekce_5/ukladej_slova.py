slova = list()

while len(slova) < 3:
    slovo = input("Zadej slovo ze 4 písmen : ")
    if len(slovo) != 4:
        print("Slovo není dlouhé 4 znaky")
    elif slovo in slova:
        print("Slovo", slovo, "je již uložené")
    else:
        slova.append(slovo)
print("Už mám uložené 3 slova")