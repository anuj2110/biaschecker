import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle 
import csv
import warnings
warnings.filterwarnings('ignore')


#df = pd.read_csv('bank-full.csv')
#df=np.array(df)
with open("df", "rb") as f:
	df = pickle.load(f)


corpus = ['Age','AGE', 'Gender','GENDER','disability','DISABILITY','marital','MARITAL',
          'MARITAL STATUS','Marital status','Marital_Status','maritalstatus''religion','RELIGION',
          'caste','CASTE','National origin','NATIONAL ORIGIN','NATIONALITY','Nationality',
          'nationality','ORIGIN','Origin','education','income source','background',
          'Number of men','Number of women','White','Black''Hispanic','State','County',
          'Latino','Country','Native','Sexuality','Mortality Rate','income','race',
          'board of education','higher secondary education','percentage','work exprience',
          'board of study','result','crime','victim sex','victim race','province',
          'african','american','CODE_GENDER','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','OCCUPATION_TYPE','Ethnicity','Language','LegalStatus',
	 'MaritalStatus','Annual Income','sex','gender','age','ethnicity']

corpus = np.array(corpus)

corpus

df.columns.values

our_columns  = np.array(df.columns.values)
our_columns

corpus = np.char.lower(corpus)
corpus

common = np.intersect1d(corpus, our_columns)
common

#temp=getattr(df,common[2]).value_counts()/len(df)
#temp.count()


percent = []
bias = []

for c in common:
        vals = (getattr(df,c).value_counts()/len(df))*100
        no_of_vals = vals.count()
        if no_of_vals < 6 and no_of_vals > 1:
            # print('The percentage count of',c)
            # print(vals)
            percent.append(vals)
        req_per = 100/no_of_vals
        for v in vals:
            if v < req_per or v > req_per:
                # print('Bias exists in ',c)
                bias.append(c)
                break
            
with open("percent","wb") as f:
        pickle.dump(percent,f)
        
        
with open("bias","wb") as f:
        pickle.dump(bias,f)       
        
        
    
