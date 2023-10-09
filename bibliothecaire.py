from personne import *
from emprunt import *

class Bibliothecaire(Personne):
    def __init__(self,nom,prenom,adresse,numero):
        Personne.__init__(self,nom,prenom,adresse)
        set_numero(self,numero)
        self.__nb_emprunt=0
        
    def set_numero(self,numero):
        self.__numero=numero
    
    def get_numero(self,numero):
        return self.__numero
    
    def set_nb_emprunts(self,nombre):
        self.__nb_emprunt=nombre
        
    def get_nb_emprunts(self):
        return self.__nb_emprunt
    
        
    