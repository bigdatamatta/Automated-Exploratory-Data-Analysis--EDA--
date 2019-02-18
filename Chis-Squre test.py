# Using Chisquare Test
from scipy.stats import chi2_contingency
from scipy.stats import chi2
import pandas as pd
import numpy as np 


#Module Chi-square
def ChiSquare_Test(df, ycol, xcol, alpha):
    '''
    Documentation : 
    --------------
    * df     : Dataframe Name
    * ycol   : y target (Categorcal Variable)
    * xcol   : x target array (Categorical Variable)
    * alpha  : Significance Level (0.1, 0.05, 0.01)
    
    ex:
    # 1. Define Dataframe
    df_categ = df_categ_list
    
    # 2. Input y column  
    y = 'SaleType'
    
    # 3. Input X columns
    x =['Street','LandContour','LandSlope']
   
   # 4. Significance Level 
    a = 0.05
    
    # 5. Chi-Square Analisys 
    ChiSquare_Test(df = df_categ_list, ycol=y, xcol= x, alpha= a)
    '''
    result = {}
    
    #Looping for every x variable in Dataframe
    for x in xcol :
        crosstab = pd.crosstab(df[ycol],df[x])
        _, p, _, _ = chi2_contingency(crosstab)
        
        #logic
        if p <= alpha :
            result[x] = 'Correlated'
        else :
            result[x] = 'Not Correlated'
    
    #The result will be created to the pandas dataframe 
    df = pd.DataFrame.from_dict(result, orient='Index', columns=['Decision'])
    df.index.name='Colname'
    
    return df