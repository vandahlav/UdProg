# Domácí úkol 1 - PIŠKVORKY
# Zadání
Napište hru piškvorky na 3x3 polích. Program nemusí umět vyhodnocovat, že nějaký
hráč vyhrál, ani kolizi v políčkách. Hráči zadávají souřadnice do konzole,
průběh hry je vykreslen želví grafikou.

# Zpracování 
Nejprve byly naimportovány potřebné knihovny pro zpracování úlohy pomocí funkce import. Následně byla stanovena proměnná t jako zkrácenina turtle pro rychlejší a snažší práci. Vykreslení čtvercové mřížky proběhne po zadání libovolného čísla uživatelem, který tak určí počet řádků a sloupců. Lze však pouze zadat přirozená čísla. V ostatních případech program spadne (pokud se jedná o záporná čísla, vyzve k opětovnému zadání nového čísla). Délka strany jednotlivých čtverců ve čtvercové síti je fixně nastavena na 40, ale je možné ji stejně jako počet sloupců a řádků nechat definovat uživatele. K vykreslení čtvercové mřížky byly použity tři for cykly. Značky pro křížek a kolečko jsou definovány pomocí funkce. Rovněž je jim přidělena rozdílná barva pro větší přehlednost. 

Samotné střídání hráčů probíhá přes while cyklus, kde podmínku tvoří počet tahů ve hře (tedy počet řádků * počet sloupců). Na začátku je X hráči (cross_player) nastavena hodnota True. Pomocí vnořené funkce if načteme souřadnice od prvního hráče. V případě nekorektního zápisu je vyzván k opakovanému zadání. Pokud by zadal jiný datový typ než int, program spadne. Metodou setpose je želvě nastavena pozice kde následně vykreslí křížek. Na konci tahu hráče jedna je změněna hodnota proměnné cross_player na její negaci. Tím je umožněno v dalším tahu hrát O hráči. Pokaždé, když zahraje jeden hráč, dojde k odečtení -1 od proměnné pocet_policek, čímž postupně dojde k vyčerpání všech tahů ve hře, program vypíše game over a hra končí. 

# Závěr
Tento skript neurčuje vítěze hry. Hráči mohou svůj tah hrát do totožného pole a vykreslená mřížka tak nemusí být využita celá. 