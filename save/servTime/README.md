# Nástroje

## serv.time tools
Nástroje na úpravu serv.time se používají pro snížení všech serv.time hodnot v SAVE,
jelikož serverový čas je uložený v příliš malé integer hodnotě a po několika letech
běhu serveru tato hodnota začne přetékat.

Nástroje na úpravu serv.time v save se skládají z dvou klíčových skriptů

1. composeSettingsSuspects.py
2. moveServTime.py

V dalších sekcích jsou jednotlivé skripty popsány.

## composeSettingsSuspects.py
Skript je napsán pro python 3.8+

Tento skript projde save, který se mu předá na vstupu, a pokusí se uhodnout všechny proměnné,
které obsahují hodnotu serv.time. Takto identifikované hodnoty se pak vypíší do souboru,
jehož jméno se skládá z jména vstupního souboru a přidaným suffixem `-servtimes.txt`.

Hodnoty jsou vypsané ve formátu, kterému rozumí druhý skript `moveServTime.py`,
který už skutečně provádí transformaci serverového času. Tyto identifikované hodnoty se pak
mohou vložit na začátek souboru `moveServerTime.py` do proměnné `settings`, pokud na serveru
proběhl od posledního běhu vývoj, který přidal další proměnné k opravě.

**Pozor: všechny hodnoty je třeba projít a upravit, je-li to nezbytné. Settings hodnoty v
souboru `moveServerTime.py` mohou být napsány chytřeji (například s použitím sekce ANY, nebo regulárního výrazu).**

Skript je třeba aplikovat na oba save soubory zvlášť.
1. sphereworld.scp
2. spherechars.scp

Příklad použití:
```
python3 ./composeSettingsSuspects.py -t 2000000000 -f ../sphereworld.scp
python3 ./composeSettingsSuspects.py -t 2000000000 -f ../spherechars.scp
```

## moveServerTime.py
Skript je napsán pro python 3.8+

Tento skritp provede skutečné posunutí serverového času u všech identifikovaných záznamů.
Definice identifikovaných atributů i s popisem jednotlivých možností nastavení je
hned na začátku souboru v proměnné `settings`.

Skript je třeba aplikovat na oba save soubory zvlášť.
1. sphereworld.scp
2. spherechars.scp

**POZOR: Čas je třeba posunout s identickou hodnotou `-t` pro oba save soubory**

**POZOR: Úpravu save je třeba provádět nad posledním save při přerušeném provozu tak,
aby se následně sphere mohla znovu spustit z upraveného save.**

Příklad použití:
```
python3 ./moveServerTime.py -t 2000000000 -f ../sphereworld.scp
python3 ./moveServerTime.py -t 2000000000 -f ../spherechars.scp
```