#Načte modul který obsahuje funkce náhodnosti
import random

#Variable hraci slouží pro jmenování Hráče1 a Hráče2
hraci = ["Hráč1", "Hráč2"]

#Variable skore je slovník určen podle typu závorek (může se později přidat více hráčů díky tomu že jsem použil slovník) vytváří aktuální hodnoty skóre pro každého hráče
#Je tam hrac: 0 aby hra začala s nula body pro oba hráče
skore = {hrac: 0 for hrac in hraci}

#Definivání funkce kostky která používá modul random aby generovala čísla (mezi 1,6) funkce vrátí-(odevzdá) hodnotu tohoto hodu
def hod_kostkou():
    return random.randint(1,6)

#Definování funkce bodování která vezme ty čísla co nahoře kód vyhodil a vrátí-(odevzdá) jejich hodnotu, ale u jedničky odevzdá 100 a u 6 odevzdá 60.
def body(cislo):
    if cislo == 1:
        return 100
    elif cislo == 6:
        return 60
    else:
        return cislo

#Definování funkce samotné hry
def chicago():
#Udělá smyčku kde se kód bude opakovat 6 krát
   for kolo in range(7):
       for hrac in hraci:
           body_hrac = 0
           for _ in range(3):
               hod = hod_kostkou()
               body_hrac += body(hod)
           skore[hrac] += body_hrac
           print(f"{hrac}) hodil {body_hrac} bodů  v {kolo + 1}. kole. Celkové skóre je {skore[hrac]}.")
           
#Použije funkci print způsob formátování řetěžce je f-string (proto tam je to f) 
print(f"Vítězem je {vitez} s celkovým skóre {skore[vitez]} bodů!")

chicago()

#Variable vitez najde hráče s nejvyšším celkovým skórem po tom co hra skončí, používá funkci max() která najde největší hodnotu
#klíč lambda řekne funkci max() aby porovnala hráče[X] podle skore takže jako variable vitez se uloží jméno hráče s největším skóre
vitez = max(skore, key=lambda x: skore[x])
