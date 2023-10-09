

from datetime import date
from lecteur import *
from livre import *

# ***** classe Emprunt *****        
class Emprunt:
    def __init__(self,numero_lecteur,numero_livre,numero_bibliothecaire):
        self.__numero_lecteur = numero_lecteur
        self.__numero_livre = numero_livre
        self.__date = date.isoformat(date.today())
        self.__numero_biblithecaire=numero_bibliothecaire

    def get_numero_lecteur(self):
        return self.__numero_lecteur
        
    def get_numero_livre(self):
        return self.__numero_livre

    def get_numero_bibliothecaire(self):
        return self.__numero_bibliothecaire
        
    def get_date(self):
        return self.__date

    def __str__(self):
        return 'Emprunt - Numero lecteur : {}, Numero livre: {}, Numero biblithecaire :  {}, Date : {}'.format(self.__numero_lecteur,self.__numero_livre,self.__numero_bibliothecaire,self.__date)
  
