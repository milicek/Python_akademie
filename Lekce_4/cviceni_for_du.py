zamestnanci_raw = """
Helena Vybíralová
Wendy Štrumlová
Marie Vybíralová
Stanislav Bechyňka
Zdeňka Urbánková
Lukáš Riečan
Veronika Koudelová
Františka Vorlová
Ilie Seleš
Martin Železný
Petra Niklesová
Bohumil Skok
Jakub Šmíd
Jarmila Procházková
Dagmar Hlavatá
Jiří Nguyen Thanh
Marie Franková
Dana Ulrichová
Jana Hranická
Hana Budošová
Ivan Široký
Květoslava Jiráčková
Pavel Przywara
Josef Umlauf
Tomáš Granzer
Miroslav Kuba
Miloslava Adámková
Marie Karlíková
Jaroslav Hronský
Vlasta Karlíková
Andrea Žatková
Zuzana Lokočová
Ondřej Ptáček
Zdeněk Najman
Tereza Šebešová
Antonie Skokánková
Jan Lion
Václav Vecko
František Vajgl
Adéla Kavková
Amália Vacková
Anna Pažická
Ivo Pustějovský
Antonín Pavela
Jitka Adamová
Libuše Hamroziová
Drahomíra Balzerová
Marek Suchánek
Petr Vavrinec
Jonáš Stuchlý
Jaromír Pecen
Markéta Kyliánková
Marina Pečenková
Ivana Perdochová
Michaela Drápalová
Michael Mentlík
Rudolf Špičák
Žaneta Holá
Blanka Lišková
Eva Svatoňová
Rostislav Hoang
Martina Kalivodová
Milan Hruška
Zdenka Marková
Lenka Schambergerová
Růžena Martinů
Věra Řezanková
Marie Pečenková
Miloš Váchal
Jaroslava Hrubá
Petr Pecen
Pavla Konvicová
Lucie Marešová
Květuše Zdráhalová
Vlastimila Svatošová
Zora Michalčíková
Daniel Švejnoha
Klára Brunclíková
Vladimír Bauer
Michal Slaný
Jiřina Novosadová
Karel Sršeň
Stanislava Lakosilová
Filip Černý
Alena Kubiková
Sára Kotrlová
Alois Rejlek
Božena Novotná
Maryana Nováková
Kateřina Máslová
Ladislav Dvořák
Radek Varga
Petr Dvořák
Ludmila Jaklová
Renáta Foubíková
Nikola Lehká
Dominika Riegerová
Patrik Polák
Soňa Štrbová
David Matoušek
Liubov Hollíková
Monika Poláková
Marie Jaklová
Aleš Svoboda
Roman Kolínský
Karolína Košiková
"""
seznam = dict()

for zamestnanec in zamestnanci_raw[1:-1].split("\n"):
    detail = dict()
    #print(zamestnanec)
    detail["Email"] = ((zamestnanec[0].lower()) + "." + zamestnanec.lower().split(" ")[1] + "@firma.cz")
    detail["Křestní_jmeno"] = (zamestnanec.split(" ")[0])
    detail["Příjmení"] = (zamestnanec.split(" ")[1]) 
    #print(detail)
    seznam[zamestnanec] = detail
    #break
print(seznam)    