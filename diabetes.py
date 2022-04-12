#Import libraries :
    
import numpy as np
from matplotlib import colors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd

#chargement de dataset / affichage :
    
dataset = pd.read_csv('diabetes_data_upload-1.csv')
print(dataset)



# créer une figure et un axe

a = dataset['Age']
b = dataset['class']
plt.plot(a, b)

plt.show()

# statistique avant modification :

print(dataset['Age'].describe())
print("\n")
print(dataset['Gender'].describe())
print("\n")
print(dataset['Polyuria'].describe())
print("\n")
print(dataset['Polydipsia'].describe())
print("\n")
print(dataset['sudden weight loss'].describe())
print("\n")
print(dataset['weakness'].describe())
print("\n")
print(dataset['Polyphagia'].describe())
print("\n")
print(dataset['Genital thrush'].describe())
print("\n")
print(dataset['visual blurring'].describe())
print("\n")
print(dataset['Itching'].describe())
print("\n")
print(dataset['Irritability'].describe())
print("\n")
print(dataset['delayed healing'].describe())
print("\n")
print(dataset['partial paresis'].describe())
print("\n")
print(dataset['muscle stiffness'].describe())
print("\n")
print(dataset['Obesity'].describe())
print("\n")
print(dataset['class'].describe())
print("\n")
print(dataset['visual blurring'].describe())
        

# Nettoyage de data :
# supp de la fausse colonne :
    
dataset.drop('fakecolumn', inplace=True, axis=1)


# cherche si il y a des données manquants 
      
print(dataset.isnull().sum())


#les listes des valeurs util

VALID_Gender = ['Male', 'Female']
VALID_class = ['Positive', 'Negative']
VALID_Polydipsia= ['Yes', 'No']
VALID_Polyuria= ['Yes', 'No']
    
def check_Gender(Gender):
    
    #verification si la valeur de la case appartient à la liste qui contient Male et Female
    
    if Gender not in VALID_Gender:
        
        #l'affichage de la valeur pour la remplacer
        
        print(' - "{}" n\', nous le modefiants.' \
            .format(Gender))
            
            #recherche de les valeurs et les remplacer
            
        if format(Gender) =='homme':
            return 'Male'
        if format(Gender) =='femme':
            return 'female'
    return Gender

def check_YESNO(Polydipsia):
    
    #verification si la valeur de la case appartient à la liste qui contient Yes et No
    
    if Polydipsia not in VALID_Polydipsia:
        print(' - "{}" n\', nous le modefiants.' \
            .format(Polydipsia))
    return Polydipsia
                 
def check_Polyuria(Polyuria):
    
    #verification si la valeur de la case appartient à la liste qui contient Yes et No
    
    if Polyuria not in VALID_Polyuria:
        
        #l'affichage de la valeur pour la remplacer
        
        print(' - "{}" n\', nous le modefiants.' \
            .format(Polyuria))
            
            #recherche de la valeur et la remplacer
            
        if format(Polyuria) =='Oui':
            return 'Yes'
    return Polyuria
def check_sudden(sudden_weight_loss):
    
    #verification si la valeur de la case apartient à la liste qui contient Yes et No
    
    if sudden_weight_loss not in VALID_Polyuria:
        
        #l'affichage de la valeur pour la remplacer
        
        print(' - "{}" n\', nous le modefiants.' \
            .format(sudden_weight_loss))
            
            #recherche de la valeur et la remplacer
            
        if format(sudden_weight_loss) =='Oui':
            return 'Yes'
    return sudden_weight_loss
def check_oui(week):
    
    #verification si la valeur de la case apartient à la liste qui contient Yes et No
    
    if week not in VALID_Polyuria:
        
        #l'affichage de la valeur pour la remplacer
        
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
            
        #recherche de la valeur et la remplacer
        
        if format(week) =='oui':
            return 'Yes'
    return week

#fonction qui remplace Na par No
 
def check_Polyphagia(week):
    
    #verification si la valeur de la case apartient à la liste qui contient Yes et No
    
    if week not in VALID_Polyuria:
        
        #l'affichage de la valeur pour la remplacer
        
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
            
        #recherche de la valeur et la remplacer
        
        if format(week) =='na':
            return 'No'
    return week

#fonction qui remplace Na et 0 par No et 1 par Yes

def check_del(week):
    
    #verification si la valeur de la case appartient à la liste qui contient Yes et No
    
    if week not in VALID_Polyuria:
        
        #l'affichage de la valeur pour la remplacer
        
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
            
        #recherche de les valeurs et les remplacer
        
        if format(week) =='na':
            return 'No'
        if format(week) =='0':
            return 'No'
        if format(week) =='1':
            return 'Yes'
    return week

#fonction qui remplace Nan par No

def check_Genital(week):
    
    #verification si la valeur de la case appartient à la liste qui contient Yes et No
    
    if week not in VALID_Polyuria:
        
        #l'affichage de la valeur pour la remplacer
        
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
            
            #recherche de la valeur et la remplacer
            
        if format(week) =='Nan':
            return 'No'
    return week

#fonction qui remplace none par No

def check_itch(week):
    
    #verification si la valeur de la case appartient à la liste qui contient Yes et No
    
    if week not in VALID_Polyuria:
        
        #l'affichage de la valeur pour la remplacer
        
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
            
            #recherche de la valeur et la remplacer
            
        if format(week) =='none':
            return 'No'
    return week
def check_class(Polydipsia):
    
    #verification si la valeur de la case apartient à la liste qui contient Positive et Negative
    
    if Polydipsia not in VALID_class:
        print(' - "{}" n\', nous le modefiants.' \
            .format(Polydipsia))
    return Polydipsia


#fonction qui convert Male par 1 et Female par 0

def mod_gender(gender):
        if format(gender) == 'Male':
            return 1
        if format(gender) == 'Female':
            return 0
        return gender
    
    
#fonction qui convert Yes par 1 et No avec 0  

def mod_YESNO(Polyuria):
    
        if format(Polyuria) =='Yes':
            return 1
        if format(Polyuria) =='No':
            return 0
        return Polyuria
    
    
#fonction qui convert Positive par 1  et Negative par 0

def mod_Class(Class):
        if format(Class) =='Positive':
            return 1
        if format(Class) =='Negative':
            return 0
        return Class

#suppression de la ligne

index=dataset.loc[dataset['visual blurring']=='ozjdzjod']
print(index)
dataset=dataset.drop(61,axis=0)


#apple des fonctions qui remplacent les données aberants

dataset['Gender'] = dataset['Gender'].apply(check_Gender)
dataset['Polyuria'] = dataset['Polyuria'].apply(check_Polyuria)
dataset['Polydipsia'] = dataset['Polydipsia'].apply(check_YESNO)
dataset['sudden weight loss'] = dataset['sudden weight loss'].apply(check_sudden)
dataset['weakness'] = dataset['weakness'].apply(check_oui)
dataset['Polyphagia'] = dataset['Polyphagia'].apply(check_Polyphagia)
dataset['Genital thrush'] = dataset['Genital thrush'].apply(check_Genital)
dataset['Itching'] = dataset['Itching'].apply(check_itch)
dataset['Irritability'] = dataset['Irritability'].apply(check_YESNO)
dataset['delayed healing'] = dataset['delayed healing'].apply(check_del)
dataset['partial paresis'] = dataset['partial paresis'].apply(check_oui)
dataset['muscle stiffness'] = dataset['muscle stiffness'].apply(check_YESNO)
dataset['Alopecia'] = dataset['Alopecia'].apply(check_YESNO)
dataset['Obesity'] = dataset['Obesity'].apply(check_YESNO)
dataset['class'] = dataset['class'].apply(check_class)


#affichage les données aprés netoyage des données 

print(dataset)

#appel des fonctions qui remplaces les données non numérique avec 0 et 1


dataset['Gender'] = dataset['Gender'].apply(mod_gender)
dataset['Polyuria'] = dataset['Polyuria'].apply(mod_YESNO)
dataset['Polydipsia'] = dataset['Polydipsia'].apply(mod_YESNO)
dataset['sudden weight loss'] = dataset['sudden weight loss'].apply(mod_YESNO)
dataset['weakness'] = dataset['weakness'].apply(mod_YESNO)
dataset['Polyphagia'] = dataset['Polyphagia'].apply(mod_YESNO)
dataset['Genital thrush'] = dataset['Genital thrush'].apply(mod_YESNO)
dataset['visual blurring'] = dataset['visual blurring'].apply(mod_YESNO)
dataset['Itching'] = dataset['Itching'].apply(mod_YESNO)
dataset['Irritability'] = dataset['Irritability'].apply(mod_YESNO)
dataset['delayed healing'] = dataset['delayed healing'].apply(mod_YESNO)
dataset['partial paresis'] = dataset['partial paresis'].apply(mod_YESNO)
dataset['muscle stiffness'] = dataset['muscle stiffness'].apply(mod_YESNO)
dataset['Alopecia'] = dataset['Alopecia'].apply(mod_YESNO)
dataset['Obesity'] = dataset['Obesity'].apply(mod_YESNO)
dataset['class'] = dataset['class'].apply(mod_Class)


#affichage les données aprés remplacements les données non numérique avec 0 et 1

print(dataset)



# Assign values a X and y variables:
    
X = dataset.iloc[:,400].values
y = dataset[':,400..500'].values


# Split dataset into random train and tests:
    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


# normalis # standare

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# l'algo knn est predifini dans sklearn :

classifier = KNeighborsClassifier(n_neighbors=2)


# manipulation de notre calssifier dans les data train and test avec fitting :

classifier.fit(X_train, y_train)


# Prédictions data with classifier knn :
    
y_predict = classifier.predict(X_test)


# Print results:
# affichage de matrice de confusion pour les test de qualité de model :

print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))
