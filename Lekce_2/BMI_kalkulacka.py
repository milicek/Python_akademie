jmeno = "Martin"
vaha = 128
vyska = 1.87
bmi = vaha / (vyska ** 2)

#Rozhodnutí jaká kategorie
if bmi > 40 :
    kategorie = "Těžká obezita"
elif bmi > 30 :
    kategorie = "Obezita"
elif bmi > 25 :
    kategorie = "Mírná nadváha"
elif bmi > 18.5 :
    kategorie = "Zdravá váha"
else :
    kategorie = "Podvýživa"

print(jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie)
