"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Uryč
email: michal.uryc@seznam.cz
"""

# Tuple s připravenými texty
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#registrovaní uživatelé
users = {"bob" : "123",
         "ann" : "pass123",
         "mike" : "password123",
         "liz" : "pass123"}
oddelovac = 40 * "-"

#zadání uživatelského jména
jmeno = "bob" #input("zadejte uživatelské jméno : ")
heslo = "123" #input("Zadejte heslo : ")
if users.get(jmeno) != heslo:
    print("unregistered user, terminating the program..")
    exit()

#výpis hlavičky na obrazovku
print(oddelovac)
print("Welcome to the app, ", jmeno)
print("We have 3 texts to be analyzed.")
print(oddelovac)

#výběr textu
text = input("Enter a number btw. 1 and 3 to select: ")
if text.isdigit():
    text = int(text)
else:
    print("You don´t print number")
    exit()

if 0 < text > 3:
    print("You don´t print number between 1 and 3")
    exit()

#list_vyberu = list()
texts[(text- 1)].replace("-", " ")
list_vyberu = texts[(text- 1)].replace("-", " ").split()
print(list_vyberu)

#pomocné proměnné
prvni_velke = 0
prvni_male = 0
vse_velke = 0
cislo = 0
soucet = 0
delka_slov = dict()

for slovo_vyberu in list_vyberu:
    #pokud je za slovem čárka nebo tečka, umaž ji
    if slovo_vyberu[-1] == "," or slovo_vyberu[-1] == ".":
        slovo_vyberu = slovo_vyberu[:-1]


    #pokud slovo začíná číslem, nejedná se o slovo ale o číslo
    if slovo_vyberu[0].isnumeric():
        upravene_slovo = ""
        for znak in slovo_vyberu:
            if znak.isnumeric():
                upravene_slovo = upravene_slovo + str(znak)
    else:
        upravene_slovo = slovo_vyberu

    if upravene_slovo[0].isupper() and upravene_slovo[1:-1].islower():
        prvni_velke += 1
    elif upravene_slovo.islower():
        prvni_male += 1
    elif upravene_slovo.isupper():
        vse_velke += 1
    elif upravene_slovo.isnumeric():
        cislo += 1
        soucet += int(upravene_slovo) 

    #spočítáme počet slov podle délek slov
    delka = len(upravene_slovo)
    if delka not in delka_slov:
        delka_slov[delka] = 1
    else:
        delka_slov[delka] =  delka_slov[delka] + 1

#vypíšeme co se po nás chce
print(oddelovac)    
print("There are ", len(list_vyberu), "words in the selected text")
print("There are ", prvni_velke, "titlecase words.")
print("There are ", vse_velke, "uppercase words.")
print("There are ", prvni_male, "lowercase words.")
print("There are ", cislo, "numeric strings.")
print("The sum of all numbers :", soucet)
print(oddelovac)

#Teď vyrobíme a vytiskneme graf
print("LEN|     OCCURENCES        |NR.")
print(oddelovac)
for legenda in range(1, (len(delka_slov)) + 1):
    #pokud není výskyt slov s určitým počtem písmen tak nevypíšeme a přeskočíme
    if not delka_slov.get(legenda):
        continue
    #při výpisu jednociferných čísel zarovnáme doprava ať to líp vypadá
    elif len(str(legenda)) == 1:
        ocislovani = " " + str(legenda)
    else:
        ocislovani = legenda
    #a teď už to vypíšeme a zarovnáme pravou strnu podle počtu výskytů
    print(ocislovani, "|",
         delka_slov[legenda] * "*",
         (20 - delka_slov[legenda]) * " ",
         "|", delka_slov[legenda])
