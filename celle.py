# Klassedefinisjon for Celle

class Celle:
   def  __init__(self):
       self._status = "doed"

    # Sett status til doed
   def settDoed(self):
       self._status = "doed"

    # Sett status til levende
   def settLevende(self):
       self._status = "levende"

    # Sjekk status, returnerer True eller False
   def erLevende(self):
       if self._status == "levende":
           return True
       else:
           return False

   # Hent tegn, avhengig av cellens status
   def hentStatusTegn(self):
       if self.erLevende():
           return "O"
       else:
           return "."
