mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
#vypíšeme pozdrav a nabídku
print("Vítejte v naší aplikaci Destinatio")
print(cara)
print(nabidka)
print(cara)

#vstup dat
destinace = input("Číslo destinace :")
jmeno = input("Jméno :")
prijmeni = input("Příjmení :")
email = input("Email :")
print(cara)

#výpočet indexu z čísla destinace
destinace = int(destinace) - 1

#a jdeme vypsat potvrzení
print("Děkuji,", jmeno, "za objednávku,")
print("Cílová destinace :", mesta[destinace], "Cena jízdenky :", ceny[destinace])
print("Na váš email", email, "jsme vám poslali lístek")
print(cara)