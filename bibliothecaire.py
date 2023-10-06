from personne import *

class Bibliothecaire(Personne):
    def __init__(self,nom,prenom,adresse,numero):
        Personne.__init__(self,nom,prenom,adresse)
        self.__numero=numero