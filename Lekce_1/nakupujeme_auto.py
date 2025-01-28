mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000
cena_2_merc = 2 * mercedes
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = 2 * (rolls_royce + vybava)
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc
print("Sleva na Mercedes :", sleva_merc)
print("Cena za dva Mercedesy :", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce :",cena_merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkvou výbavou :", cena_2_rolls_s_vybavou)
print("Cena za Mercedes s příplatkovou výbavou :", cena_merc_s_vybavou)
print("Cena za Mercedes po slevě :", merc_se_slevou)