# ALOS-
  *le code finale implementer duranat le parcours de l'atelier ALOS*


## Etape1: 
Installation des outils (python, ide , bibliothèques, ...)


## Etape2:
Telecharger de dataset (diabets)


## Etape3:
Changemenet de format du dataset (excel --> csv)

## Etape3:
- Afficher les dataset /chergement
 ```
 dataset = pd.read_csv('diabetes_data_upload-1.csv')
 print(dataset)
 ```
![image](https://user-images.githubusercontent.com/62666792/162850534-51a1874a-cef0-4402-a04f-bd206484ab86.png)

 Affichage des statistiques descriptives des colonnes pour plus de détails (count, max, min , ..)
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
![image](https://user-images.githubusercontent.com/62666792/162850831-4b9dac48-22e8-4644-b4aa-b1d3ecc794ed.png)
![image](https://user-images.githubusercontent.com/62666792/162850857-200cab04-0333-48ca-8a6f-d9ecbb5a3837.png)


# Etape4:
#### NETTOYAGE de données :
 - suppression une fausse colonne(fakecolumn)
 ```
data.drop('fakecolumn', inplace=True, axis=1)
 ```
 - verification des case vide ( les donne manquants )
 
 ` print(data.isnull().sum()) `
 
 ![image](https://user-images.githubusercontent.com/62666792/162850921-eaa70985-730b-44f8-82b3-928f35a5c8c5.png)

 
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
  ![image](https://user-images.githubusercontent.com/62666792/162851071-1c89e728-97ed-484f-bb1b-f9dc150bfaf2.png)

 - modification des formats de données(données alphabétique --> données numérique 1, 0)
 
   pour l'attribut gender comme exemple :
   ```
   def mod_gender(gender):
        if format(gender) == 'Male':
            return 1
        if format(gender) == 'Female':
            return 0
        return gender
     ```
     ![image](https://user-images.githubusercontent.com/62666792/162851202-932ac255-1ba4-406f-9fb7-42a4f017f136.png)

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
 ![image](https://user-images.githubusercontent.com/62666792/162851248-8fb3c08f-8b88-441e-92ec-31b2cf6bde40.png)

## Etape6:

Comparaison entres les premiers graphes(avant le nettoyage) et les derniers (apres le nettoyage)

## Etape7:
####  l'entrainement et test:
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
![image](https://user-images.githubusercontent.com/62666792/162851305-25f4eca5-e8b4-4fc1-b9a9-42bd74fe5ee4.png)


### l'affichage est sur le fichier (rslt)

