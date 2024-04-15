#Načte modul který obsahuje funkce náhodnosti
import random

#Definivání funkce kostky která používá modul random aby generovala čísla (mezi 1,6) funkce vrátí-(odevzdá) hodnotu tohoto hodu
def hod_kostkou():
    return random.randit(1,6)

#Definování funkce bodování která vezme ty čísla co nahoře kód vyhodil a vrátí-(odevzdá) jejich hodnotu, ale u jedničky odevzdá 100 a u 6 odevzdá 60.
def body(cislo):
    if cislo == 1:
        return 100
    elif cislo == 6:
        return 60
    else:
        return cislo

