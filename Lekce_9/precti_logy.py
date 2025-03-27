def precti_logy(soubor: str):
    with open(soubor, mode="r", encoding='utf-8') as f:
        return f.readlines()
    
print(precti_logy("Lekce_9/logy.txt"))