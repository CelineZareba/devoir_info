from personne import Personne

class Conservateur(Personne):
    def __init__(self,nom,prenom,adresse,nom_bibliotheque): 
        Personne.__init__(self,nom,prenom,adresse)
        self.__bibliotheque=self.get_bibliotheque() 

    def get_bibliotheque(self):
        return self.__bibliotheque

    def set_bibliotheque(self,nom_bibliotheque):
        self.__bibliotheque=nom_bibliotheque
    
        

    
    
