import os

os.chdir((os.getcwd()) +"\\Lekce_6\\vytvor_slozky\\ ")

slozky = ["obrazky", "texty", "gify"]

for slozka in slozky:
    if os.path.exists((os.getcwd() + "\\" + slozka)):
        print("Složka ", slozka, " již existuje") 
    else:
        print("Tvořím složku : ", slozka)
        os.mkdir(slozka)   
print("Všechny složky existují")
