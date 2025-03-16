operator = {"+", "-"}

print('Sčítání:        "+"')
print('Odčítání:       "-"')
print(20 * "-")
while True:
    operace = input("Vyber si operátor : ")
    if operace in operator:
        prvni_cislo = int(input("Zadej první číslo: "))
        druhe_cislo = int(input("Zadej druhé číslo: "))
        if operace == "+":
            print(prvni_cislo, operace, druhe_cislo, "=", (prvni_cislo + druhe_cislo))
        else:
            print(prvni_cislo, operace, druhe_cislo, "=", (prvni_cislo - druhe_cislo))
        dalsi = input("Chcete proést další operaci? zadejte 'a' pokud ano, každé jiné zadání znamená ne: ")
        if dalsi != "a":
            break
    else:
        print("Nezadali jste správný operátor, zkuste to znovu")