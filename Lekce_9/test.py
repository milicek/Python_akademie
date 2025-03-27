def zapis_zpravu_do_txt_souboru(zprava: str,
                                jmeno_souboru: str
                               ):
    # Vytvoříme spojení s daným argumentem a souborem ..
    muj_txt_soubor = open(jmeno_souboru,
                          mode='w',
                          encoding='UTF-8')

    # zapíšeme zprávu do souboru ..
    muj_txt_soubor.write(zprava)

    # uzavřeme spojení se souborem.
    muj_txt_soubor.close()
    
    
zapis_zpravu_do_txt_souboru("Ahoj Jardo", "test_text.txt")