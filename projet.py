# import des librairies dont nous aurons besoin
import pandas as pd


# chargement et affichage des données

data = pd.read_csv('C://Users//yygvyubu//Desktop//ALOS--main//ALOS--main//diabetes_data_upload-1.csv')
#affichage des données
print(data)
# supp de la fausse colonne
        
data.drop('fakecolumn', inplace=True, axis=1)
# cherche si il y a des données manquants       
print(data.isnull().sum())
#les listes des valeurs 
VALID_Gender = ['Male', 'Female']
VALID_class = ['Positive', 'Negative']
VALID_Polydipsia= ['Yes', 'No']
VALID_Polyuria= ['Yes', 'No']
    
def check_Gender(Gender):
    #verification si la valeur de la case apartient à la lise qui contient Male et Female
    if Gender not in VALID_Gender:
        #l'affichage de la valeur pour la remplacer
        print(' - "{}" n\', nous le modefiants.' \
            .format(Gender))
            #recherche de les valeurs et les remplacé
        if format(Gender) =='homme':
            return 'Male'
        if format(Gender) =='femme':
            return 'female'
    return Gender

def check_YESNO(Polydipsia):
    #verification si la valeur de la case apartient à la lise qui contient Yes et No
    if Polydipsia not in VALID_Polydipsia:
        print(' - "{}" n\', nous le modefiants.' \
            .format(Polydipsia))
    return Polydipsia
                 
def check_Polyuria(Polyuria):
    #verification si la valeur de la case apartient à la lise qui contient Yes et No
    if Polyuria not in VALID_Polyuria:
        #l'affichage de la valeur pour la remplacer
        print(' - "{}" n\', nous le modefiants.' \
            .format(Polyuria))
            #recherche de la valeur et la remplacé
        if format(Polyuria) =='Oui':
            return 'Yes'
    return Polyuria
def check_sudden(sudden_weight_loss):
    #verification si la valeur de la case apartient à la lise qui contient Yes et No
    if sudden_weight_loss not in VALID_Polyuria:
        #l'affichage de la valeur pour la remplacer
        print(' - "{}" n\', nous le modefiants.' \
            .format(sudden_weight_loss))
            #recherche de la valeur et la remplacé
        if format(sudden_weight_loss) =='Oui':
            return 'Yes'
    return sudden_weight_loss
def check_oui(week):
    #verification si la valeur de la case apartient à la lise qui contient Yes et No
    if week not in VALID_Polyuria:
        #l'affichage de la valeur pour la remplacer
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        #recherche de la valeur et la remplacé
        if format(week) =='oui':
            return 'Yes'
    return week
#fonction qui remplace Na par No 
def check_Polyphagia(week):
    #verification si la valeur de la case apartient à la lise qui contient Yes et No
    if week not in VALID_Polyuria:
        #l'affichage de la valeur pour la remplacer
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        #recherche de la valeur et la remplacé
        if format(week) =='na':
            return 'No'
    return week
#fonction qui remplace Na et 0 par No et 1 par Yes
def check_del(week):
    #verification si la valeur de la case apartient à la lise qui contient Yes et No
    if week not in VALID_Polyuria:
        #l'affichage de la valeur pour la remplacer
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        #recherche de les valeurs et les remplacé
        if format(week) =='na':
            return 'No'
        if format(week) =='0':
            return 'No'
        if format(week) =='1':
            return 'Yes'
    return week
#fonction qui remplace Nan par No
def check_Genital(week):
    #verification si la valeur de la case apartient à la lise qui contient Yes et No
    if week not in VALID_Polyuria:
        #l'affichage de la valeur pour la remplacer
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
            #recherche de la valeur et la remplacé
        if format(week) =='Nan':
            return 'No'
    return week
#fonction qui remplace none par No
def check_itch(week):
    #verification si la valeur de la case apartient à la lise qui contient Yes et No
    if week not in VALID_Polyuria:
        #l'affichage de la valeur pour la remplacer
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
            #recherche de la valeur et la remplacé
        if format(week) =='none':
            return 'No'
    return week
def check_class(Polydipsia):
    #verification si la valeur de la case apartient à la lise qui contient Positive et Negative
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
index=data.loc[data['visual blurring']=='ozjdzjod']
print(index)
data=data.drop(61,axis=0)
#apple des fonctions qui remplacent les données aberants
data['Gender'] = data['Gender'].apply(check_Gender)
data['Polyuria'] = data['Polyuria'].apply(check_Polyuria)
data['Polydipsia'] = data['Polydipsia'].apply(check_YESNO)
data['sudden weight loss'] = data['sudden weight loss'].apply(check_sudden)
data['weakness'] = data['weakness'].apply(check_oui)
data['Polyphagia'] = data['Polyphagia'].apply(check_Polyphagia)
data['Genital thrush'] = data['Genital thrush'].apply(check_Genital)
data['Itching'] = data['Itching'].apply(check_itch)
data['Irritability'] = data['Irritability'].apply(check_YESNO)
data['delayed healing'] = data['delayed healing'].apply(check_del)
data['partial paresis'] = data['partial paresis'].apply(check_oui)
data['muscle stiffness'] = data['muscle stiffness'].apply(check_YESNO)
data['Alopecia'] = data['Alopecia'].apply(check_YESNO)
data['Obesity'] = data['Obesity'].apply(check_YESNO)
data['class'] = data['class'].apply(check_class)
#affichage les données aprés netoyage des données 
print(data)

#appel des fonctions qui remplaces les données non numérique avec 0 et 1
data['Gender'] = data['Gender'].apply(mod_gender)
data['Polyuria'] = data['Polyuria'].apply(mod_YESNO)
data['Polydipsia'] = data['Polydipsia'].apply(mod_YESNO)
data['sudden weight loss'] = data['sudden weight loss'].apply(mod_YESNO)
data['weakness'] = data['weakness'].apply(mod_YESNO)
data['Polyphagia'] = data['Polyphagia'].apply(mod_YESNO)
data['Genital thrush'] = data['Genital thrush'].apply(mod_YESNO)
data['visual blurring'] = data['visual blurring'].apply(mod_YESNO)
data['Itching'] = data['Itching'].apply(mod_YESNO)
data['Irritability'] = data['Irritability'].apply(mod_YESNO)
data['delayed healing'] = data['delayed healing'].apply(mod_YESNO)
data['partial paresis'] = data['partial paresis'].apply(mod_YESNO)
data['muscle stiffness'] = data['muscle stiffness'].apply(mod_YESNO)
data['Alopecia'] = data['Alopecia'].apply(mod_YESNO)
data['Obesity'] = data['Obesity'].apply(mod_YESNO)
data['class'] = data['class'].apply(mod_Class)

#affichage les données aprés remplacements les données non numérique avec 0 et 1
print(data)
