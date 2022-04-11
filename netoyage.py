# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np

# chargement et affichage des données

data = pd.read_csv('C://Users//yygvyubu//Desktop//ALOS--main//ALOS--main//diabetes_data_upload-1.csv')
print(data)
data.drop('fakecolumn', inplace=True, axis=1)
        
print(data.isnull().sum())
VALID_Gender = ['Male', 'Female']
VALID_class = ['Positive', 'Negative']



                  
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


def check_class(Polydipsia):
    if Polydipsia not in VALID_class:
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
def check_sudden(sudden_weight_loss):
    if sudden_weight_loss not in VALID_Polyuria:
        print(' - "{}" n\', nous le modefiants.' \
            .format(sudden_weight_loss))
        if format(sudden_weight_loss) =='Oui':
            return 'Yes'
        
                    
        
    return sudden_weight_loss
def check_week(week):
    if week not in VALID_Polyuria:
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        if format(week) =='oui':
            return 'Yes'
        
                    
        
    return week

def check_Polyphagia(week):
    if week not in VALID_Polyuria:
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        if format(week) =='na':
            return 'No'
        
                    
        
    return week

def check_del(week):
    if week not in VALID_Polyuria:
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        if format(week) =='na':
            return 'No'
        if format(week) =='0':
            return 'No'
        if format(week) =='1':
            return 'Yes'
        
        
                    
        
    return week

def check_Genital(week):
    if week not in VALID_Polyuria:
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        if format(week) =='Nan':
            return 'No'
        
                    
        
    return week
def check_itch(week):
    if week not in VALID_Polyuria:
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        if format(week) =='none':
            return 'No'
        
                    
        
    return week
def check_sup(week):
    if week not in VALID_Polyuria:
        print(' - "{}" n\', nous le modefiants.' \
            .format(week))
        
        
                    
        
    return week




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

index=data.loc[data['visual blurring']=='ozjdzjod']
print(index)
data=data.drop(61,axis=0)

print(data)
