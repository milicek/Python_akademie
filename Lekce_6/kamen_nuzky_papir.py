from random import randint

moznosti = ['kamen', 'nuzky', 'papir']
hrac = input("Kámen, nůžky, papír? : ")
pocitac = moznosti[(randint(0, 2))]

print("Hráč: ", hrac)
print("Počítač: ", pocitac)


if hrac == pocitac:
    print("remiza")
elif hrac == "kamen":
    if pocitac == "nuzky":
        print("Vyhrál jsi.")
    else:
        print("Prohrál jsi.")
elif hrac == "papir":
    if pocitac == "kamen":
        print("Vyhrál jsi.")
    else:
        print("Prohrál jsi.")    
else:
    if pocitac == "papir":
        print("Vyhrál jsi.")
    else:
        print("Prohrál jsi.")    
