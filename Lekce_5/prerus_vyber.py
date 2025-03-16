ovoce = ["jablko", "banan", "citron", "pomeranc"]

print("Dostupné ovoce:", ", ".join(ovoce))

while True :
    vyber = input("VYBER Z DOSTUPNÉHO OVOCE: ")
    if vyber in ovoce:
        print("Bezva toto ovoce je v nabídce")
        break
    else:
        print("Ovoce není v nabídce")
