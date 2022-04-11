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
 - affichage des statistiques descriptives des colonnes pour plus de détails (count, max, min , ..)
 ```
   print(data['Age'].describe())
   print("\n")
   print(data['Gender'].describe())
   print("\n")
   print(data['Polyuria'].describe())
   print("\n")
   print(data['Polydipsia'].describe())
   print("\n")
   print(data['sudden weight loss'].describe())
   print("\n")
   print(data['weakness'].describe())
   print("\n")
   print(data['Polyphagia'].describe())
   print("\n")
   print(data['Genital thrush'].describe())
   print("\n")
   print(data['visual blurring'].describe())
   print("\n")
   print(data['Itching'].describe())
   print("\n")
   print(data['Irritability'].describe())
   print("\n")
   print(data['delayed healing'].describe())
   print("\n")
   print(data['partial paresis'].describe())
   print("\n")
   print(data['muscle stiffness'].describe())
   print("\n")
   print(data['Obesity'].describe())
   print("\n")
   print(data['class'].describe())
   print("\n")
   print(data['visual blurring'].describe())
   ```
 - verification des case vide ( les donne manquants )
 
 ' print(data.isnull().sum()) '
 
 - modification de quelques valeurs écrites en francais (oui , non --> yes, no)
   
 ```
 
   data['Gender'] = data['Gender'].apply(check_Gender)
   data['Polyuria'] = data['Polyuria'].apply(check_Polyuria)
   data['Polydipsia'] = data['Polydipsia'].apply(check_Polydipsia)
   data['sudden weight loss'] = data['sudden weight loss'].apply(check_sudden)
   data['weakness'] = data['weakness'].apply(check_week)
   data['Polyphagia'] = data['Polyphagia'].apply(check_Polyphagia)
   data['Genital thrush'] = data['Genital thrush'].apply(check_Genital)
   data['visual blurring'] = data['visual blurring'].apply(check_sup)
   data['Itching'] = data['Itching'].apply(check_itch)
   data['Irritability'] = data['Irritability'].apply(check_Polydipsia)
   data['delayed healing'] = data['delayed healing'].apply(check_del)
   data['partial paresis'] = data['partial paresis'].apply(check_week)
   data['muscle stiffness'] = data['muscle stiffness'].apply(check_Polydipsia)
   data['Alopecia'] = data['Alopecia'].apply(check_Polydipsia)
   data['Obesity'] = data['Obesity'].apply(check_Polydipsia)
   data['class'] = data['class'].apply(check_class)

  ```  
 - modification des formats de données(données alphabétique --> données numérique 1, 0)
 - suppression d'une ligne qui contient une fausse valeur (ozjdzjod)
  ```
   index=data.loc[data['visual blurring']=='ozjdzjod']
   print(index)
   data=data.drop(61,axis=0)
  ```
 - la normalisation et la standarisation de dataset 
 ```
 scaler = StandardScaler()
 ```

## Etape5:
l'affichage des graphes (plots)
 ``` 
 a = dataset['Age']
 b = dataset['class']
 plt.plot(a, b)

 plt.show()
 ```


## Etape6:

comparaison entres les premiers graphes(avant le nettoyage) et les derniers (apres le nettoyage)

## Etape7:
l'entrainement et test:
 - assignement des valeurs a x et y variables pour la dévision dde dataset (test and train)
 - dévision du dataset aléatoirement entre l'entrainement (80%) et test (20%) 
```
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```

## Etape8:
 - choix d'algorithme : K-nearest neighbour KNN , car notre data donne positive et négative (deux classe)
 - manipulation d'algorithme pour la classification de data et prediction avec le classificateur
 ```
 classifier = KNeighborsClassifier(n_neighbors=2)
 classifier.fit(X_train, y_train)
 y_predict = classifier.predict(X_test)
 ```


# etape9:
Affichage les resultats(matrice de confusion et le rapport)
```
print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))
```


