# ALOS-
  *le code finale implementer duranat le parcours de l'atelier ALOS*


## Etape1: 
installation des outils (python, ide , bibliothèques, ...)


## Etape2:
telecharger de dataset (diabets)


## Etape3:
changemenet de format du dataset (excel --> csv)


# Etape4:
#### NETTOYAGE de données :
 - supp une fausse colonne(fakecolumn)
 ```
 dataset = pd.read_csv('diabetes_data_upload-1.csv')
 print(dataset)
 ```
 - affichage des statistiques  descriptives des colonnes pour plus de détails (count, max, min , ..)
 - modification de quelques valeurs écrites en francais (oui , non --> yes, no)
 - modification des formats de données(données alphabétique --> données numérique 1, 0)
 - supp d'une ligne qui contient une fausse valeur (ozjdzjod)



## Etape5:
affichage des graphes (plots)


# etape6:
comparaison entres les premiers graphes(avant le nettoyage) et les derniers (apres le nettoyage)

# etape7:
assignement des valeurs a x et y variables pour la dévision dde dataset (test and train)

# etape8:
dévision du dataset aléatoirement entre l'entrainement (80%) et test (20%) et standarisation 

# etape9:
choix d'algorithme : K-nearest neighbour KNN 

# etape10:
manipulation d'algorithme pour la classification de data 
prediction avec le classificateur
affichage des resultats(matrice de confusion et le rapport)
