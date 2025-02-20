novy_uzivatel_3 = {
    "jmeno": "Lukáš",
    "prijmeni": "Holinka",
    "vek": 28,
    "hobby": ("fotbal", "hry", "pratele"),
    "kontakt": {  # Nestovaný slovník
        "telefon": "000 123 456 789",
        "email": "lukas@gmail.com",
        "web": "www.lukas.cz"
    }
}
print(novy_uzivatel_3["kontakt"]["email"])
print(novy_uzivatel_3.keys())