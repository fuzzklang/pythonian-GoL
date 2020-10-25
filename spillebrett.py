# Klassedefinisjon for Spillebrett
# matrix av celler

from random import randint
import random
from celle import Celle


class Spillebrett:
    def __init__(self, rader, kolonner, p=1/3):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjonsnummer = 0

        # Konstruer rutenett - noestet liste med celler
        self._rutenett = self._konstruerRutenett(self._rader, self._kolonner)
        self._generer(p)	# p = sannsynlighet for at en gitt er celle levende ved start

        
    def _konstruerRutenett(self, rader, kolonner):
        rutenett = []
        # Legg til hver rad som en egen liste:
        for rad_idx in range(rader):
            rutenett.append([])
            # Legg til celler likt antall kolonner, for hver rad:
            for elem in range(kolonner):
                nyCelle = Celle()
                rutenett[rad_idx].append(nyCelle)
        return rutenett


    def tegnBrett(self):
        self._toemVindu()   # Toem terminalvindu

        # Tegn brett:
        for rad in self._rutenett:
            for celle in rad:
                print(celle.hentStatusTegn(), end="")
            print()
        print("Generasjon: {} – Antall levende celler: {}".format(self._generasjonsnummer, self.finnAntallLevende()))


    def _toemVindu(self):
        # Privat metode for aa "toemme" terminalvindu
        if self._rader >= 60:    # Hvis mer enn 100 rader, print kun en linje
            print()
        else:                    # Ellers: print flere, toem vindu
            antallLinjer = 60 - self._rader
            for i in range(antallLinjer):
                print()
 

    def oppdatering(self):
        settLevendeListe = []
        settDoedListe = []

        # Sjekk hver enkelt celle
        for rad_koordinat, rad in enumerate(self._rutenett):
            for kolonne_koordinat, celle in enumerate(rad):
                naboer = self.finnNabo(rad_koordinat, kolonne_koordinat)	# Finn naboer til hver celle
                antallLevendeNaboer = self._finnAntallLevendeNaboer(naboer)	# Beregne antall levende naboer
                if celle.erLevende() == False:		# Sett levende jf. spillets regler
                    if antallLevendeNaboer == 3:
                        settLevendeListe.append(celle)
                elif celle.erLevende() == True:		# Sett levende jf. spillets regler
                    if antallLevendeNaboer < 2 or antallLevendeNaboer > 3:
                        settDoedListe.append(celle)

        # Gjoer oppdatering:
        for celle in settLevendeListe:
            celle.settLevende()

        for celle in settDoedListe:
            celle.settDoed()

        self._generasjonsnummer += 1

        
    def _finnAntallLevendeNaboer(self, naboliste):
        # Returnerer antall levende celler i en liste over celler
        teller = 0
        for celle in naboliste:
            if celle.erLevende():
                teller += 1
        return teller
            
        
    def finnAntallLevende(self):
        # Returner totalt antall levende celler paa brettet
        antallLevende = 0
        for rad in self._rutenett:
            for celle in rad:
                if celle.erLevende() == True:
                    antallLevende += 1
        return antallLevende


    def _generer(self, p=1/3):
        # Gjennomgaa hver celle i noestet liste:
        # p = sannsynlighet for at en gitt celle er levende ved start

        for rad in self._rutenett:
            for celle in rad:
                if random.random() < p:
                    celle.settLevende()
                # Jf. oppgaveformulering:
                #if randint(0,2) == 0:    # 1/3 sjans for levende
                #    celle.settLevende()


    def finnNabo(self, rad_koordinat, kolonne_koordinat):
        naboer = []

        # Tar utgangspunkt i en 3x3 liste over alle naboKoordinater rundt et gitt koordinat.
        x = kolonne_koordinat	# x-akse-posisjon
        y = rad_koordinat	# y-akse-posisjon

        for i in range(-1, 2):
            for j in range(-1, 2):
                naboKoordinat = (x+i, y+j)
                # Sjekker at naboKoordinat er innenfor rutenett, og ikke lik koordinatet gitt som argument
                if self._koordErInnenfor(rad_koordinat=naboKoordinat[1], kolonne_koordinat=naboKoordinat[0]) and not naboKoordinat == (x,y):
                    # Hvis kriterier oppfylt, finn celle i rutenett vha. av koordinater og legg til i listen naboer
                    rad = naboKoordinat[1]
                    kolonne = naboKoordinat[0]
                    naboCelle = self._rutenett[rad][kolonne]
                    naboer.append(naboCelle)
        return naboer

    
    def _koordErInnenfor(self, rad_koordinat, kolonne_koordinat):
        # Privat metode for aa sjekke om koordinat er utenfor rutenett.
        # Listene er 0-indeksert, altsaa maa posisjon vaere mellom 0 og (len(noestetListet) - 1)
        # Returner True/False
        return (0 <= rad_koordinat < self._rader) and (0 <= kolonne_koordinat < self._kolonner)
