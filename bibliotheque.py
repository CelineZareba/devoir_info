from datetime import date

# ***** classe Personne *****
class Personne:
    def __init__(self,nom,prenom,adresse):
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        
    def __str__(self):
        return f"Classe Personne - Nom : {self.__nom}, Prenom : {self.__prenom}, Adresse : {self.__adresse}"
        
    def set_nom(self,nom):
        self.__nom = nom
        
    def get_nom(self):
        return self.__nom
        
    def set_prenom(self,prenom):
        self.__prenom = prenom
        
    def get_prenom(self):
        return self.__prenom
        
    def set_adresse(self,adresse):
        self.__adresse = adresse
        
    def get_adresse(self):
        return self.__adresse
    

# ***** classe Livre *****          
class Livre:
    def __init__(self,titre,auteur,numero,nb_total):
        self.__titre = titre        
        self.__auteur = auteur
        self.__numero = numero
        self.__nb_total = nb_total
        self.__nb_dispo = nb_total

    def set_auteur(self,auteur):
        self.__auteur = auteur
        
    def get_auteur(self):
        return self.__auteur
        
    def set_titre(self,titre):
        self.__titre = titre
        
    def get_titre(self):
        return self.__titre
        
    def set_numero(self,numero):
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero
    
    def set_nb_total(self,nb_total):
        self.__nb_total = nb_total
        
    def get_nb_total(self):
        return self.__nb_total

    def set_nb_dispo(self,nb_dispo):
        self.__nb_dispo = nb_dispo
        
    def get_nb_dispo(self):
        return self.__nb_dispo
        
    def __str__(self):
        return 'Livre - Auteur : {}, Titre : {}, Numero : {}, Nb total : {}, Nb dispo : {}'.format(self.__auteur,self.__titre,self.__numero,self.__nb_total,self.__nb_dispo)

# ***** classe Lecteur *****        
class Lecteur(Personne):
    def __init__(self,nom,prenom,adresse,numero):
        Personne.__init__(self,nom,prenom,adresse)        
        self.__numero = numero
        self.__nb_emprunts = 0
        
    def set_numero(self,numero):
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero
        
    def set_nb_emprunts(self,nb_emprunts):
        self.__nb_emprunts = nb_emprunts
        
    def get_nb_emprunts(self):
        return self.__nb_emprunts
        
    def __str__(self): #Permet d'afficher les proprietes de l'objet avec la fonction print
        return 'Lecteur - Nom : {}, Prenom : {}, Adresse : {}, Numero : {}, Nb emprunts : {}'.format(self.get_nom(),self.get_prenom(),self.get_adresse(),self.__numero,self.__nb_emprunts)

# ***** classe Emprunt *****        
class Emprunt:
    def __init__(self,numero_lecteur,numero_livre,numero_bibliothecaire):
        self.__numero_lecteur = numero_lecteur
        self.__numero_livre = numero_livre
        self.__date = date.isoformat(date.today())
        self.__numero_bibliothecaire = numero_bibliothecaire

    def get_numero_lecteur(self):
        return self.__numero_lecteur
        
    def get_numero_livre(self):
        return self.__numero_livre

    def get_numero_bibliothecaire(self):
        return self.__numero_bibliothecaire
        
    def get_date(self):
        return self.__date

    def __str__(self):
        return 'Emprunt - Numero lecteur : {}, Numero livre: {}, Numero bibliothecaire :  {}, Date : {}'.format(self.__numero_lecteur,self.__numero_livre,self.__numero_bibliothecaire,self.__date)

#***classe Bibliothécaire***

class Bibliothecaire(Personne):
    def __init__(self,nom,prenom,adresse,numero):
        Personne.__init__(self,nom,prenom,adresse) #utilisation du constructeur de Personne
        self.set_numero(numero)
        self.__nb_emprunt=0 #par defaut le bibliothécaire n'a réalisé aucun emprunt
        
    def set_numero(self,numero):
        self.__numero=numero
    
    def get_numero(self):
        return self.__numero
    
    def set_nb_emprunts(self,nombre):
        self.__nb_emprunt=nombre
        
    def get_nb_emprunts(self):
        return self.__nb_emprunt

#*** classe Conservateur***

class Conservateur(Personne):
    def __init__(self,nom,prenom,adresse,nom_bibliotheque): 
        Personne.__init__(self,nom,prenom,adresse) #utilisation du constructeur de Personne
        self.set_bibliotheque(nom_bibliotheque) 

    def get_bibliotheque(self):
        return self.__bibliotheque

    def set_bibliotheque(self,nom_bibliotheque):
        self.__bibliotheque=nom_bibliotheque

###DEFINITION DE LA CLASSE BIBLIOTHEQUE

class Bibliotheque:
    def __init__(self,nom,nom_c,prenom_c,adresse_c): #nom fait ici référence au nom de la bibliothèque et []_c aux attributs du conservateur associé
        self.__nom = nom
        self.__lecteurs = [] 
        self.__livres = []
        self.__emprunts = []
        self.__bibliothecaires=[]
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
        if b1!=None:  
            print('Le bibliothecaire est déja enregistré à la bibliothèque.')
        else:
            b=Bibliothecaire(nom,prenom,adresse,numero) #sinon, on peut créer une bibliothècaire 
            self.__bibliothecaires.append(b) #et l'ajouter à la liste des bibliothecaires de la bibliotheque
            
    def retrait_bibliothecaire(self,nom,prenom):
        b=self.chercher_bibliothecaire_nom(nom,prenom) 
        if b!=None and b.get_nb_emprunts()==0: #on vérifie que le bibliothècaire fait bien parti du personnel de la bibliothèque
            self.__bibliothecaires.remove(b) #dans ce cas, on peut l'enlever de la liste des bibliothècaires
            return True                
        else:
            return False


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
            if b.get_nom() == nom and b.get_prenom()==prenom:
                return b
        return None
        
    def chercher_bibliothecaire_numero(self,numero):
        for bib in self.__bibliothecaires:
            if bib.get_numero() == numero :
                return bib
        return None
            
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
            bibliothecaire=self.chercher_bibliothecaire_numero(numero_bibliothecaire)
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
            
    
    
    
            
    
        
        
           
