# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np

# chargement et affichage des données

data = pd.read_csv('C://Users//yygvyubu//Desktop//ALOS--main//ALOS--main//diabetes_data_upload-1.csv')
print(data)
        
print(data.isnull().sum())
VALID_Gender = ['Male', 'Female']


                  
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

VALID_GENDER_M = [0, 1]

def mod_gender(gender):
    if gender not in VALID_GENDER_M:
        if format(gender) == 'Male':
            return 1
        if format(gender) == 'Female':
            return 0
    return gender

VALID_Polyuria_m = [0, 1]

def mod_Polyuria(Polyuria):
    if Polyuria not in VALID_Polyuria_m:
        if format(Polyuria) =='Yes':
            return 1
        if format(Polyuria) =='No':
            return 0
    return Polyuria

VALID_class_m = [0, 1]

def mod_Class(Class):
    if Class not in VALID_class_m:
        if format(Class) =='Positive':
            return 1
        if format(Class) =='Negative':
            return 0
    return Class

data['Gender'] = data['Gender'].apply(check_Gender)
data['Gender'] = data['Gender'].apply(mod_gender)
data['Polyuria'] = data['Polyuria'].apply(mod_Polyuria)
data['Polydipsia'] = data['Polydipsia'].apply(check_Polydipsia)

data['Polyuria'] = data['Polyuria'].apply(mod_Polyuria)
data['Polydipsia'] = data['Polydipsia'].apply(mod_Polyuria)
data['sudden weight loss'] = data['sudden weight loss'].apply(mod_Polyuria)
data['weakness'] = data['weakness'].apply(mod_Polyuria)
data['Polyphagia'] = data['Polyphagia'].apply(mod_Polyuria)
data['Genital thrush'] = data['Genital thrush'].apply(mod_Polyuria)
data['visual blurring'] = data['visual blurring'].apply(mod_Polyuria)
data['Itching'] = data['Itching'].apply(mod_Polyuria)
data['Irritability'] = data['Irritability'].apply(mod_Polyuria)
data['delayed healing'] = data['delayed healing'].apply(mod_Polyuria)
data['partial paresis'] = data['partial paresis'].apply(mod_Polyuria)
data['muscle stiffness'] = data['muscle stiffness'].apply(mod_Polyuria)
data['Alopecia'] = data['Alopecia'].apply(mod_Polyuria)
data['Obesity'] = data['Obesity'].apply(mod_Polyuria)
data['class'] = data['class'].apply(mod_Class)

VALID_visual_blurring = ['Yes', 'No']
                  
def check_visual_blurring (visual_blurring):
    if visual_blurring not in VALID_visual_blurring:
        print(' - "{}" n\', nous le modefiants.' \
            .format(visual_blurring))
        if format(visual_blurring) =='Oui':
            return 'Yes'
                
    return visual_blurring

data['visual_blurring'] = data['visual_blurring'].apply(check_visual_blurring)


print(data)
