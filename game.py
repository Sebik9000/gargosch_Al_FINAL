#Načte modul, který obsahuje funkce náhodnosti
import random

#Variable "hraci" slouží pro jmenování Hráče1 a Hráče2
hraci = ["Hráč1", "Hráč2"]

#Variable skore je slovník, který vytváří aktuální hodnoty pro každého hráče
#Je tam hrac: 0 aby hra začala s nula body pro oba hráče
skore = {hrac: 0 for hrac in hraci}

print("Vítám vás ve hře chicago, v této hře jsou dva hráči, oba hází tři krát za sebou a mají 3 kostky, ale hodí jedničku tak se jim přičte 100 bodů, a když šestku tak 60 bodů.")

print("Dosažený počet bodů za všechny hody se zapíše a hráč s nejvíce body vyhrává.")

#Definivání funkce "hod_kostkou", která používá modul random pro generování čísel mezi 1 a 6, funkce vrátí hodnotu tohoto hodu
def hod_kostkou():
    return random.randint(1,6)

#Definování funkce "body", která vezme číslo vygenerované funkcí "hod_kostkou" a vrátí jeho hodnotu. U jedničky vrátí 100 a u šestky 60
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
#Smyčka, která se opakuje 3 krát pro 3 hody kostkou
           for _ in range(3):
               hod = hod_kostkou()
               body_hrac += body(hod)
           skore[hrac] += body_hrac
           print(f"{hrac}) hodil {body_hrac} bodů v {kolo + 1}. kole. Celkové skóre je {skore[hrac]}.")
           
#Zavolá samotnou hru
chicago()

#Variable vitez najde hráče s nejvyšším celkovým skórem po tom co hra skončí, používá funkci max() která najde největší hodnotu
#klíč lambda řekne funkci max() aby porovnala hráče[X] podle skore takže jako variable vitez se uloží jméno hráče s největším skóre
vitez = max(skore, key=lambda x: skore[x])

#Použije funkci print způsob formátování řetěžce je f-string (proto tam je to f) 
print(f"Vítězem je {vitez} s celkovým skóre {skore[vitez]} bodů!")
