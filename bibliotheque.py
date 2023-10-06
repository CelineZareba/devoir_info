from lecteur import Lecteur
from livre import Livre
from emprunt import Emprunt
from bibliothecaire import *

class Bibliotheque:
	def __init__(self,nom):
		self.__nom = nom
		self.__lecteurs = []
		self.__livres = []
		self.__emprunts = []
        self.__bibliothecaires=[]

	def __str__(self):
		return '{} {}'.format(
			self.__class__.__name__,
			self.get_nom()
		)
		
	def get_nom(self):
		return self.__nom
		
	def ajout_lecteur(self,nom,prenom,adresse,numero):
		assert not self.chercher_lecteur_numero(numero)
		self.__lecteurs.append(Lecteur(nom,prenom,adresse,numero))
		
	def chercher_lecteur_numero(self,numero):
		for l in self.__lecteurs:
			if l.get_numero() == numero:
				return l
		return None
		
	def chercher_lecteur_nom(self,nom,prenom):
		for l in self.__lecteurs:
			if l.get_nom() == nom and l.get_prenom() == prenom:
				return l
		return None

	def ajout_livre(self,titre,auteur,numero,nb_total):
		assert not self.chercher_livre_numero(numero)
		# cf. programme de test : chercher_livre_titre doit renvoyer
		# un livre unique, pas une liste. Donc il ne peut y avoir
		# qu'un seul livre avec un titre donné...
		assert not self.chercher_livre_titre(titre)
		self.__livres.append(Livre(titre,auteur,numero,nb_total))
		
	def chercher_livre_numero(self,numero):
		for l in self.__livres:
			if l.get_numero() == numero:
				return l
		return None
	
	def chercher_livre_titre(self,titre):
		for l in self.__livres:
			if l.get_titre() == titre:
				return l
		return None
	
	def affiche_lecteurs(self):
		for l in self.__lecteurs:
			print(l)
			
	def affiche_livres(self):
		for l in self.__livres:
			print(l)

	def emprunt_livre(self,numero_lecteur,numero_livre):
		lecteur = self.chercher_lecteur_numero(numero_lecteur)
		livre = self.chercher_livre_numero(numero_livre)
		if lecteur == None:
			print("Emprunt impossible : lecteur non trouvé")
			return
		if livre == None:
			print("Emprunt impossible : livre non trouvé")
			return
			
		dispo = livre.get_nb_dispo()
		if not dispo > 0:
			print("Emprunt impossible : plus d'exemplaire disponible")
			return
		
		emprunt = self.chercher_emprunt(numero_lecteur,numero_livre)
		assert emprunt == None
		
		emprunt = Emprunt(numero_lecteur,numero_livre)
		assert not emprunt == None
		self.__emprunts.append(emprunt)
		
		livre.set_nb_dispo(dispo-1)
		lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()+1)
	
	def affiche_emprunts(self):
		for e in self.__emprunts:
			print(e)
	
	def retour_livre(self, numero_lecteur, numero_livre):
		e = self.chercher_emprunt(numero_lecteur,numero_livre)
		if e == None:
			print("Retour impossible, emprunt non trouvé")
			return
		self.__emprunts.remove(e)
		
		lecteur = self.chercher_lecteur_numero(numero_lecteur)
		assert not lecteur == None
		lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()+1)
		
		livre = self.chercher_livre_numero(numero_livre)
		assert not livre == None
		dispo = livre.get_nb_dispo()
		assert dispo < livre.get_nb_total()
		livre.set_nb_dispo(dispo+1)
		
	def chercher_emprunt(self,numero_lecteur,numero_livre):
		for e in self.__emprunts:
			if e.get_numero_lecteur() == numero_lecteur and e.get_numero_livre() == numero_livre:
				return e
		return None
		
	def retrait_livre(self,numero_livre):
		livre = self.chercher_livre_numero(numero_livre)
		assert not livre == None
		if not livre.get_nb_dispo() == livre.get_nb_total():
			print("Retrait impossible, emprunts en cours")
			return None
		self.__livres.remove(livre)
		return livre
	
	def retrait_lecteur(self,numero_lecteur):
		lecteur = self.chercher_lecteur_numero(numero_lecteur)
		assert not lecteur == None
		if not lecteur.get_nb_emprunts() == 0:
			print("Retrait impossible, emprunts en cours")
			return None
		self.__lecteurs.remove(lecteur)
		return lecteur
    
    def add_bibliothecaire(self,b):
        if b not in self.__bibliothecaires:
            self.__bibliothecaires.append(b)
        else:
            print('Bibliothecaire déjà enregistré')
        
    def remove_bibliothecaire(self,b):
        if b in self.__bibliothecaires
            self.__bibliothecaires.remove(b)
        else:
            