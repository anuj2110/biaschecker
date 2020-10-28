'''
Making the imports for the analytics and web app.
'''
import pandas as pd
import numpy as np
import streamlit as st
import pickle
from os import path
import os
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Bias checker') # App starts here

option = st.sidebar.selectbox("Choose between following",["Instructions","Example","Try the bias checker"]) # * These are the options on the sidebar

if option == "Instructions": # This will show the first page which shows instructions
    st.write("""
        ## You can use this tool in following manner
        1. Go to Try the bias checker option from the sidebar options
        2. Upload the csv you want to check bias for and wait for the results to be processed and displayed.
        Have a nice day 😊
    """)
    
    st.write("\n \n \n")

    st.write("""
    
    
        Thumb Rule while inputting a dataset to this module:  
        The **Y** variable (the predicted variable) should be renamed as **‘y’** , in the dataset provided in order to iterate and procure the results. 
        
        **For example, if the predicted variable/output variable in the dataset is with the name ‘Job Status’ should be renamed as ‘y’**
   
    """)

    st.write("\n \n \n")

    st.write("""
    ```
        Programming Language used: Python  
        Packages used:  NumPy, pandas, matplotlib, pickle, sklearn, streamlit  
        Cloud Application Platform: Streamlit Share  
        Hosting service: Git  
        Others: Jupyter Notebook, Spyder
    ```
    """)    
elif option == "Example": # This will show the example
    st.write("""
        ## Below is an example showing how the results will be displayed.
    """)
    df = pd.read_csv("student-mat.csv")
    st.dataframe(df.style.highlight_max(axis=0))
    with open("df","wb") as f:
        pickle.dump(df,f)
    os.system('python model.py')
                    
    with open("percent", "rb") as f:
        percent= pickle.load(f)
                    
    with open("bias", "rb") as f:
        bias = pickle.load(f)
    if(len(bias)==0 or len(percent)==0):
        st.markdown('**The dataset does not have any _bias_**')
    else:
        st.markdown('**The _bias_ exists in**')
        for b in bias:
            st.subheader(b)
        st.write('**The class distribution in the categorical columns is**')
        for p in percent:
            st.dataframe(p,500,400)
    os.remove("df")
    os.remove("bias")
    os.remove("percent")
elif option == "Try the bias checker":# This is the main page of the app
    
    st.write("""
        **Note: Please keep the name of the target value as __y__ **
    """)
    df=None
    multiple_files=None 

    st.write("""
        ### Please upload the csv file you want to check bias for. 
    """)
    
    multiple_files = st.file_uploader('Enter a csv file',type=["csv"])
    
    try:
        df_=pd.read_csv(multiple_files)
        df =df_
    except Exception as e:
        st.write("""
            Please provide a csv file
        """)

    if df is not None:
        st.dataframe(df.style.highlight_max(axis=0))
        try:
            with open("df","wb") as f:
                pickle.dump(df,f)
            os.system('python model.py')
                            
            with open("percent", "rb") as f:
                percent= pickle.load(f)
                            
            with open("bias", "rb") as f:
                bias = pickle.load(f)
            if(len(bias)==0 or len(percent)==0):
                st.markdown('**The dataset does not have any _bias_**')
            else:
                st.markdown('**The _bias_ exists in**')
                for b in bias:
                    st.subheader(b)
                    temp=type(df[b].iloc[0])
                    if(temp!=str):
                        st.write('Below is the distribution for this column')
                        fig, ax = plt.subplots()
                        ax.hist(df['age'],facecolor='green', alpha=0.5)
                        st.pyplot(fig)
                    else:
                        st.write('*The class distribution in this columns*')
                        for p in percent:
                            st.dataframe(p,500,400)
                        cnt=df[b].value_counts().to_frame()
                        fig, ax = plt.subplots()
                        ax.bar(list(cnt.index),cnt['sex'],facecolor='green')
                        st.pyplot(fig)
                        st.write('Bar plot of this column')
            os.remove("df")
            os.remove("bias")
            os.remove("percent")
        
            
        except Exception as e:
            st.write("""
                    Sorry something went wrong on backend. Please retry again with correct inputs
                """)

        st.write("""
                ### Below is the feature importances
            """)
        try:
            df=df.dropna()
            label_encoder = preprocessing.LabelEncoder() 
            df=df.apply(preprocessing.LabelEncoder().fit_transform)
            y = df["y"].to_numpy()
            collist = df.columns.tolist()
            collist.remove("y")
            x_ = df[collist]
            x = df[collist].to_numpy()

            model = ExtraTreesClassifier()
            model.fit(x,y)

            corrmat = df.corr()
            top_corr_features = corrmat.index
            sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")

            feat_importances = pd.Series(model.feature_importances_, index=x_.columns)
        
            st.header("Feature Importnaces")
            st.bar_chart(feat_importances)
            
           
        except Exception as e:
            st.write(e)  