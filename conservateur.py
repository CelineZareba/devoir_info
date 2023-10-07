from personne import Personne

class Conservateur(Personne):
    def __init__(self,nom,prenom,adresse,bibliotheque):
        Personne.__init__(self,nom,prenom,adresse)
        self.__bibliotheque=bibliotheque
    
    