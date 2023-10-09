#on importe tous les documents dont on aura besoin
from lecteur import *
from livre import *
from emprunt import *
from bibliothecaire import *
from conservateur import *
    
      
###DEFINITION DE LA CLASSE BIBLIOTHEQUE

class Bibliotheque:
    def __init__(self,nom,nom_c,prenom_c,adresse_c): #nom fait ici référence au nom de la bibliothèque et []_c aux attributs du conservateur associé
        self.__nom = nom
        self.__lecteurs = [] 
        self.__livres = []
        self.__emprunts = []
        self.__conservateur = Conservateur(nom_c,prenom_c,adresse_c,nom) #on crée le conservateur associé à la bibliothèque
        
    def get_nom(self):
        return self.__nom
        
    def get_conservateur(self):
        return self.__conservateur

###AJOUT OU RETRAIT DE LECTEUR, LIVRE ET BIBLIOTHECAIRE
    def ajout_lecteur(self,nom,prenom,adresse,numero):
        self.__lecteurs.append(Lecteur(nom,prenom,adresse,numero)) 
        
    def retrait_lecteur(self,numero):
        # On vérifie que le lecteur existe bien à la bibliothèque
        lecteur = self.chercher_lecteur_numero(numero)
        if lecteur == None:
            return False
            
        # On verifie qu'il n'a pas d'emprunt en cours
        for e in self.__emprunts:
            if e.get_numero_lecteur()==numero:
                return False
                
        # Dans ce cas, on peut ici retirer le lecteur de la liste
        self.__lecteurs.remove(lecteur)
        return True                

    
    def ajout_livre(self,auteur,titre,numero,nb_total):
        self.__livres.append(Livre(auteur,titre,numero,nb_total))
    
    def retrait_livre(self,numero):
        # On cherche le livre
        livre = self.chercher_livre_numero(numero)
        if livre == None:
            return False
            
        # On verifie que le livre n'est pas en cours d'emprunt
        for e in self.__emprunts:
            if e.get_numero_livre()==numero:
                return False
                
        # On peut ici retirer le livre de la liste
        self.__livres.remove(livre)
        return True        

    
#NOUVEAU CODE CONCERNANT LES BIBLIOTHECAIRES

    
    def ajout_bibliothecaire(self,nom,prenom,adresse,numero):
        #on vérifie tout d'abord que le bibliothècaire n'est pas déjà enregistré
        b1=self.chercher_bibliothecaire_numero(numero)
        if b1 in self.__bibliothecaires:  
            print('Le bibliothecaire est déja enregistré à la bibliothèque.')
        else:
            b=Bibliothecaire(nom,prenom,adresse,numero) #sinon, on peut créer une bibliothècaire 
            self.__bibliothecaires.append(b) #et l'ajouter à la liste des bibliothecaires de la bibliotheque
            
    def retrait_bibliothecaire(self,nom,prenom):
        b=self.chercher_bibliothecaire_nom(nom,prenom) 
        if b in self.__bibliothecaires: #on vérifie que le bibliothècaire fait bien parti du personnel de la bibliothèque
            self.__bibliothecaires.remove(b) #dans ce cas, on peut l'enlever de la liste des bibliothècaires
        else:
            print("Le bibliothècaire n'est pas enregistré dans cette bibliothèque.")

  ###CHERCHER LECTEUR, LIVRE, EMPRUNT ET BIBLIOTHECAIRE      
    def chercher_lecteur_numero(self,numero):
        for l in self.__lecteurs:
            if l.get_numero() == numero:
                return l #on a trouvé le lecteur correspondant
        return None #le numéro n'est pas attribué ià un lecteur dans ce cas

    def chercher_lecteur_nom(self,nom,prenom):
        for l in self.__lecteurs:
            if l.get_nom() == nom and l.get_prenom() == prenom:
                return l
        return None    
        
    def chercher_livre_numero(self,numero):
        for l in self.__livres:
            if l.get_numero() == numero:
                return l
        return None

    def chercher_livre_titre(self,titre):
        for l in self.__livres:
            if l.get_titre() == titre:
                return l #le livre est bien référencé à la bibliothèque
        return None  # le livre n'est pas référencé à la bibliothèque
        
    def chercher_emprunt(self, numero_lecteur, numero_livre, numero_bibliothecaire):
        for e in self.__emprunts: #on parourt la liste des emprunts de la bibliothèque
            if e.get_numero_lecteur() == numero_lecteur and e.get_numero_livre() == numero_livre and e.get_numero_bibliothecaire()==numero_bibliothecaire:
                return e #si on trouve un numero de livre et de lecteur et de bibliothecaire associé, le livre est bel et bien emprunté
        return None #le livre n'est pas emprunté
        
#NOUVEAU CODE CONCERNANT LES BIBLIOTHECAIRES 
    
    def chercher_bibliothecaire_nom(self,nom,prenom):
        for b in self.__bibliothecaires:
            if b.__nom == nom and b.__prenom==prenom:
                return b
        print("Le bibliothècaire n'est pas enregistré dans cette bibliothèque")
        
    def chercher_bibliothecaire_numero(self,numero):
        for b in self.__bibliothecaires:
            if b.__numero == str(numero) :
                return b
        print("Le bibliothècaire n'est pas enregistré dans cette bibliothèque")
            
###CREATION D'UN NOUVEL EMPRUNT OU D'UN RETOUR

    def emprunt_livre(self, numero_lecteur, numero_livre, numero_bibliothecaire):
        # On verifie que le livre existe à la bibliothèque
        livre = self.chercher_livre_numero(numero_livre)
        if livre == None:
            print('Emprunt impossible : livre inexistant')
            return None
            
        # On verifie qu'il reste des exemplaires disponibles pour ce livre
        if livre.get_nb_dispo() == 0:
            print('Emprunt impossible : plus d\'exemplaires disponibles')
            return None
            
        # On verifie que le numero de lecteur est valide
        lecteur = self.chercher_lecteur_numero(numero_lecteur)
        if lecteur == None:
            print('Emprunt impossible : lecteur inexistant')
            return None
            
        # On verifie que ce lecteur n'est pas deja entrain d'emprunter ce livre
        e = self.chercher_emprunt(numero_lecteur, numero_livre,numero_bibliothecaire)
        if e != None:
            print('Emprunt impossible : deja en cours')
            return None
            
        # On vérifie que le bibliothècaire existe 
        bibliothecaire = self.chercher_bibliothecaire_numero(numero_bibliothecaire)
        if bibliothecaire == None:
            print("Le bibliothècaire n'existe pas")
            return None
            
     # Si toutes les conditions précédentes sont validés, l'emprunt est possible, on effectue toutes les modifications nécessaires des attributs
        self.__emprunts.append(Emprunt(numero_lecteur, numero_livre, numero_bibliothecaire)) #on ajoute l'emprunt à la liste des emprunts de la bibliothèque
        livre.set_nb_dispo(livre.get_nb_dispo()-1) #on diminue le nombre d'exemplaires disponibles du livre
        lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()+1) #on augmente le nombre de livre emprunté par le lecteur
        bibliothecaire.set_nb_emprunts(bibliothecaire.get_nb_emprunts()+1) #on augmente le nombre de livre emprunté via le bibliothecaire
        return self.__emprunts[-1] #on retourne le livre qui vient d'être ajouté à la liste des emprunts (dernier élément de la liste)


    
    
    def retour_livre(self, numero_lecteur, numero_livre,numero_bibliothecaire):
        # On vérifie que l'emprunt existe
        e = self.chercher_emprunt(numero_lecteur, numero_livre,numero_bibliothecaire)
        if e != None: 
            # si c'est le cas, on le retire de la liste et on met a jour nb_emprunt pour le lecteur, nb_dispo pour le livre et nb_emprunt pour le bibliothècaire
            self.__emprunts.remove(e)
            
            #on va vérifier à chaque fois que lecteur, livre et bibliothècaire existent à la bibliothèque
            
            #on modifie les attributs du lecteur 
            lecteur = self.chercher_lecteur_numero(numero_lecteur)
            if lecteur != None : lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()-1)
                
            #on modifie les attributs du livre
            livre = self.chercher_livre_numero(numero_livre)
            if livre != None: livre.set_nb_dispo(livre.get_nb_dispo()+1)
                
            #on modifie les attributs du bibliothecaire
            bibliothecaire=self.chercher_bibliothecaire(numero_bibliothecaire)
            if bibliothecaire != None : 
                bibliothecaire.set_nb_emprunts(bibliothecaire.get_nb_emprunts()-1)
                print('Retour effectué')
                return True
            else:
                print('Aucun emprunt ne correspond à ces informations')
                return False


###AFFICHAGE DES LISTES DE LA BIBLIOTHEQUE

    
    def affiche_lecteurs(self):
        for l in self.__lecteurs:
            print(l)

    def affiche_livres(self):
        for l in self.__livres:
            print(l)           
            
    def affiche_emprunts(self):
        for e in self.__emprunts:
            print(e)
            
    def affiche_bibliothecaires(self):
        for b in self.__bibliothecaires:
            print(b)
            
    
    
    
            
    
        
        
           
