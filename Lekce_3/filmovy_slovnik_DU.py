sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62

film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}
film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}
film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}
# sjednoť předchozí 3 slovníky do jednoho slovníku 'filmy'
# .. klíčem bude jméno filmu a samotný slovník následuje
# .. jako hodnota.
#filmy = dict()
#print(film_1["jmeno"])
#filmy[str(film_1["jmeno"])] = dict(film_1)
#filmy[film_2["jmeno"]] = film_2
#filmy[film_3["jmeno"]] = film_3

filmy = {
    str(film_1["jmeno"]): dict(film_1.items()),
    str(film_2["jmeno"]): dict(film_2.items()),
    str(film_3["jmeno"]): dict(film_3.items())
}

print ("              VÍTEJTE V NAŠEM FILMOVÉM SLOVNÍKU!           ")
print(oddelovac)
print("       dostupné filmy | detaily filmu | seznam režisérů")
print(oddelovac)
pomoc_filmy = tuple(filmy.keys())
vyber_z_nabidky = input("Vyberte z nabídky : ")

if vyber_z_nabidky == ("dostupné filmy" or "detaily filmu"):
    print ("                  DOSTUPNÉ FILMY           ")
    print(oddelovac)
    print(pomoc_filmy)
    print(oddelovac)
    vyber_filmu = input("Vyber film: ")
    if filmy.get(vyber_filmu):
        print(filmy[vyber_filmu])
    else:
        print("vybraný film není v naší databázi")
elif vyber_z_nabidky == "seznam režisérů":
    print(tuple(filmy.values())[0]["reziser"], tuple(filmy.values())[1]["reziser"], tuple(filmy.values())[2]["reziser"] )
else:
    print("Toto v nabídce nemáme")


