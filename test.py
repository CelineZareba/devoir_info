from bibliotheque import *


# Creation d'une bibliotheque
b = Bibliotheque('Bibliotheque ECL','Pascal','Ray','Ecully')

# Ajout de lecteurs
b.ajout_lecteur('Duval','Pierre','rue de la Paix',1)
b.ajout_lecteur('Dupond','Laurent','rue de la Gare',2)
b.ajout_lecteur('Martin','Marie','rue La Fayette',3)
b.ajout_lecteur('Dubois','Sophie','rue du Stade',4)

# Ajout de livres
b.ajout_livre('Le Pere Goriot','Honore de Balzac',101,2)
b.ajout_livre('Les Hauts de Hurlevent','Emilie Bronte',102,2)
b.ajout_livre('Le Petit Prince','Antoine de Saint Exupery',103,2)
b.ajout_livre('L\'Etranger','Albert Camus',104,2)

# Ajout de Bibliothecaire

b.ajout_bibliothecaire('Renaud','Jean-Didier','Vertou',1)
b.ajout_bibliothecaire('Portier', 'Josselin', 'Lyon',2)
b.ajout_bibliothecaire('Girondeau', 'Ezequiel','Buenos Aires',3)
# Affichage des lecteurs, des livres, des bibliothécaires et du conservateur
print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()
print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()
print('\n---Liste des bibliothécaires:')
print('-------------------------------')
b.affiche_bibliothecaires()

# Recherches de lecteurs par numero
print('\n--- Recherche de lecteurs :')
print('-------------------------------')
lect = b.chercher_lecteur_numero(1)
if lect != None:
    print(lect)
else:
    print('Lecteur non trouve')

lect = b.chercher_lecteur_numero(6)
if lect != None:
    print(lect)
else:
    print('Lecteur non trouve')

# Recherches de lecteurs par nom
lect = b.chercher_lecteur_nom('Martin','Marie')
if lect != None:
    print(lect)
else:
    print('Lecteur non trouve')
    
lect = b.chercher_lecteur_nom('Le Grand','Paul')
if lect != None:
    print(lect)
else:
    print('Lecteur non trouve')

# Recherches de livres par numero
print('\n--- Recherche de livres :')
print('-------------------------------')
livre = b.chercher_livre_numero(101)
if livre != None:
    print('Livre trouve :',livre)
else:
    print('Livre non trouve')

livre = b.chercher_livre_numero(106)
if livre != None:
    print('Livre trouve :',livre)
else:
    print('Livre non trouve')

# Recherches de livres par titre
livre = b.chercher_livre_titre('Les Hauts de Hurlevent')
if livre != None:
    print('Livre trouve :',livre)
else:
    print('Livre non trouve')

livre = b.chercher_livre_titre('Madame Bovarie')
if livre != None:
    print('Livre trouve :',livre)
else:
    print('Livre non trouve')

#Recherche de bibliothecaire par nom
print('\n--- Recherche de bibliothécaires :')
print('-------------------------------')
bib= b.chercher_bibliothecaire_nom('Renaud', 'Jean-Didier')
if bib!=None:
    print('Bibiliothécaire trouve',bib)
else:
    print('Bibliothécaire non trouvé')
    
bib= b.chercher_bibliothecaire_nom('Moura','Lucas')
if bib!=None:
    print('Bibiliothécaire trouve',bib)
else:
    print('Bibliothécaire non trouvé')

# Recherche de bibliothecaire par numero

bib = b.chercher_bibliothecaire_numero(1)
if bib != None:
    print('Bibliothécaire trouve :',bib)
else:
    print('Bibliothécaire non trouvé')

bib = b.chercher_bibliothecaire_numero(106)
if bib != None:
    print('Bibliothécaire trouvé :',bib)
else:
    print('Bibliothécaire non trouvé')

# Quelques emprunts
print('\n--- Quelques emprunts :')
print('-------------------------------')
b.emprunt_livre(1,101,1)
b.emprunt_livre(1,104,2)
b.emprunt_livre(2,101,3)
b.emprunt_livre(2,105,1)
b.emprunt_livre(3,101,2)
b.emprunt_livre(3,104,3)
b.emprunt_livre(4,102,1)
b.emprunt_livre(4,103,2)

# Affichage des emprunts, des lecteurs des livres et des bibliothecaires
print('\n--- Liste des emprunts :')
print('-------------------------------')
b.affiche_emprunts()
print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()
print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()
print('\n--- Liste des bibliothécaires :')
print('-------------------------------')
b.affiche_bibliothecaires()

# Quelques retours de livres
print('\n--- Quelques retours de livres :')
print('-------------------------------')
b.retour_livre(1,101,1)
b.retour_livre(1,102,1)
b.retour_livre(3,104,2)
b.retour_livre(10,108,3)

# Affichage des emprunts, des lecteurs, des livres et des bibliothécaires
print('\n--- Liste des emprunts :')
print('-------------------------------')
b.affiche_emprunts()
print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()
print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()
print('\n--- Liste des bibliothécaires :')
print('-------------------------------')
b.affiche_bibliothecaires()


# Suppression de quelques livres
rep = b.retrait_livre(101)
if not rep:
    print('Retrait du livre impossible')
else:
    print('Retrait du livre effectue')

b.retour_livre(2,101,3)

rep = b.retrait_livre(101)
if not rep:
    print('Retrait du livre impossible')
else:
    print('Retrait du livre effectue')

# Suppression de quelques lecteurs
rep = b.retrait_lecteur(1)
if not rep:
    print('Retrait du lecteur impossible')
else:
    print('Retrait du lecteur effectue')

b.retour_livre(1,104,2)

rep = b.retrait_lecteur(1)
if not rep:
    print('Retrait du lecteur impossible')
else:
    print('Retrait du lecteur effectue')
    
#Suppression de quelques bibliothécaires

rep=b.retrait_bibliothecaire('Portier','Josselin')
if not rep:
    print('Retrait du bibliothécaire impossible')
else:
    print('Retrait effectué')

b.retour_livre(4,103,2)

rep=b.retrait_bibliothecaire('Portier','Josselin')
if not rep:
    print('Retrait du bibliothécaire impossible')
else:
    print('Retrait effectué')


# Affichage des emprunts, des lecteurs, des livres et des bibliothécaires
print('\n--- Liste des emprunts :')
print('-------------------------------')
b.affiche_emprunts()
print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()
print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()
print('\n--- Liste des bibliothécaires :')
print('-------------------------------')
b.affiche_bibliothecaires()



