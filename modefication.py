# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np

# chargement et affichage des données

data = pd.read_csv('C://Users//yygvyubu//Desktop//ALOS--main//ALOS--main//diabetes_data_upload-1.csv')
print(data)
        
print(data.isnull().sum())
VALID_Gender = ['Male', 'Female']
VALID_GENDER_M = [0, 1]


                  
def check_Gender(Gender):
    if Gender not in VALID_Gender:
        print(' - "{}" n\', nous le modefiants.' \
            .format(Gender))
        if format(Gender) =='homme':
            return 'Male'
        if format(Gender) =='femme':
            return 'female'
        
                    
        
    return Gender

VALID_Polydipsia= ['Yes', 'No']



                  
def check_Polydipsia(Polydipsia):
    if Polydipsia not in VALID_Polydipsia:
        print(' - "{}" n\', nous le modefiants.' \
            .format(Polydipsia))
        
        
                    
        
    return Polydipsia

VALID_Polyuria= ['Yes', 'No']



                  
def check_Polyuria(Polyuria):
    if Polyuria not in VALID_Polyuria:
        print(' - "{}" n\', nous le modefiants.' \
            .format(Polyuria))
        if format(Polyuria) =='Oui':
            return 'Yes'
        
                    
        
    return Polyuria


def mod_gender(gender):
    if gender not in VALID_GENDER_M:
        if format(gender) == 'Male':
            return 1
        if format(gender) == 'Female':
            return 0
    return gender

data['Gender'] = data['Gender'].apply(check_Gender)
data['Gender'] = data['Gender'].apply(mod_gender)
data['Polyuria'] = data['Polyuria'].apply(check_Polyuria)
data['Polydipsia'] = data['Polydipsia'].apply(check_Polydipsia)

print(data)
