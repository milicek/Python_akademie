'''Tvým úkolem bude odstraňovat písmena ze zadaného seznamu pomocí funkce `input`:
```python
pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]
```

Jakmile budou všechna písmena odstraněná, vypíše tvůj program:
```python
Seznam je prázdný!
```

Pokud zapíšeš písmeno, které v zadaném seznamu není, dostaneš upozornění:
```python
x není součástí písmen!
```

Průběh může vypadat následovně:
```python
Začátek: ['a', 'a', 'b', 'c', 'd', 'a', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? a
Zbývají písmena ['a', 'b', 'c', 'd', 'a', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? a
Zbývají písmena ['b', 'c', 'd', 'a', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? a
Zbývají písmena ['b', 'c', 'd', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? b
Zbývají písmena ['c', 'd', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? c
Zbývají písmena ['d', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? d
Zbývají písmena ['e', 'g', 'm']
ktere písmeno chceš vyhodit? e
Zbývají písmena ['g', 'm']
ktere písmeno chceš vyhodit? x
x není součástí písmen!
ktere písmeno chceš vyhodit? g
Zbývají písmena ['m']
ktere písmeno chceš vyhodit? m
Seznam je prázdný!
```'''






pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]

print(pismena)

while pismena:
    pismeno = input("Které písmeno chceš vyhodit?")
    if pismeno  in pismena:
        pismena.remove(pismeno)
        if len(pismena) == 0:
            break
        print("Zbývají písmena", pismena)
    else:
        print(pismeno, "není součástí písmen")
print("Seznam je prázdný")
