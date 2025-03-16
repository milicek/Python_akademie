import random

min_hodnota = 1
max_hodnota = 6

while True:
    print("Házím kostkou")
    hodnota = random.randint(min_hodnota, max_hodnota)
    print("Na kostce je: ", hodnota)
    if hodnota != 6:
        break
    