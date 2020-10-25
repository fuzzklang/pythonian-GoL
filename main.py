# Programmet kan kjoeres baade i interaktiv og automatisk modus
# Hvis argumentet "-a" gis ved programkall kjoeres automatisk modus ($ main.py -a)
# Ellers kjoeres interaktiv modus (som spesifisert i oppgaven)

from sys import argv
from spillebrett import Spillebrett
from time import sleep


def taInnHeltall(minimum, maksimum):
    # Tar inn heltall med grenser
    tall = int(input(""))
    while not (minimum <= tall <= maksimum):
        tall = int(input("Oppgi tall innenfor {} og {}: ".format(minimum, maksimum)))
    return tall


def taInnFlyttall(minimum, maksimum):
    # Tar inn flyttal med grenser
    tall = float(input(""))
    while not (minimum <= tall <= maksimum):
        tall = float(input("Oppgi tall innenfor {} og {}: ".format(minimum, maksimum)))
    return tall


def kjoerInteraktivt(rader, kolonner):
    # Prosedyre for aa kalle paa rette funksjoner/metoder naar den kjoerer "interaktivt".
    # Samsvarer med oppgaveformuleringen i obligen.
    spillebrett = Spillebrett(rader, kolonner)
    spillebrett.tegnBrett()
    brukervalg = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")
    while brukervalg != "q":
        spillebrett.oppdatering()
        spillebrett.tegnBrett()
        brukervalg = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")


def kjoerAutomatisk(rader, kolonner, antallGenerasjoner=10, delta=1, p=1/3):
    # Utvidelse, for aa kjoere genereringen automatisk uten taste-input fra bruker under simuleringen.
    spillebrett = Spillebrett(rader, kolonner, p)
    spillebrett.tegnBrett()
    ctr = 0

    while ctr < antallGenerasjoner:
        spillebrett.oppdatering()
        spillebrett.tegnBrett()
        sleep(delta)
        ctr += 1


def main():
    print("Vennligst oppgi antall rader og kolonner for spillet. Anbefalt rekkevidde fra 1x1 opptil 50x200")
    print("Antall rader: ", end="")
    rader = taInnHeltall(1,300)
    print("Antall kolonner: ", end="")
    kolonner = taInnHeltall(1,500)

    if "-a" in argv:
        print("--- Kjoerer i automatisk modus ---")
        print("Vennligst oppgi antall generasjoner for spillet, minimum 1: ", end="")
        antallGenerasjoner = taInnHeltall(1, 1000)
        print("Vennligst oppgi tiden mellom hver oppdatering, kan vaere et flyttall, mellom 0.05s og 10s: ", end="")
        delta = taInnFlyttall(0.05, 10)
        print("Vennligst oppgi sannsynlighet for at en celle skal vaere levende ved start, mellom 0.0 og 1.0: ", end="")
        p = taInnFlyttall(0.0, 1.0)
        kjoerAutomatisk(rader, kolonner, antallGenerasjoner, delta, p)
    else:
        kjoerInteraktivt(rader, kolonner)


main()
