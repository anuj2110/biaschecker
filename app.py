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
        1. Go to **Try the bias checker** option from the sidebar options
        2. **Upload the csv** you want to check bias for and wait for the results to be processed and displayed.
        Have a nice day 😊
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
    df = pd.read_csv("train.csv")
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
            temp=type(df[b].iloc[0])
            if(temp!=str):
                st.write('Below is the distribution for this column')
                fig, ax = plt.subplots()
                ax.hist(df[b],facecolor='green', alpha=0.5)
                st.pyplot(fig)
            else:
                st.write('*The class distribution in this columns*')
                for p in percent:
                    st.dataframe(p,500,400)
                cnt=df[b].value_counts().to_frame()
                fig, ax = plt.subplots()
                ax.bar(list(cnt.index),cnt[b],facecolor='green')
                st.pyplot(fig)
                st.write('Bar plot of this column')
    os.remove("df")
    os.remove("bias")
    os.remove("percent")
    st.write('''In this example we have taken a very famous example of titanic dataset.We can see
    above that bias may be present in sex and age. The frequency distribution of sex columns is
    heavily imbalance hence posing a potential bias towards male passengers, hence the trend in male
    passengers might affect the overall trend of the model.Also in the age column the histogram 
    seems to be a bit skewed which can be a reason of a potential bias.''')

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

    feat_importances = pd.Series(model.feature_importances_, index=x_.columns)

    st.header("Feature Importance")
    st.bar_chart(feat_importances)
    st.write(''' By the feature importance we intend to show the significance of different variables
    and their effects on the target variable. A feature with greater importance like in this example sex,
    age,fare e.t.c can affect the overall trend of the model. Now if there is a bias in very important 
    columns such as age and sex then it can severely affect the model performance in comparison to bias
    present in not so important features as they don't actually have much say in prediction. Hence the 
    motive of showing feature importance is to check weather the potential biased columns are important 
    for the model or not and according to that we can act to mitigate the bias.

    ''')



    df = pd.read_csv("bank.csv")
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
            temp=type(df[b].iloc[0])
            if(temp!=str):
                st.write('Below is the distribution for this column')
                fig, ax = plt.subplots()
                ax.hist(df[b],facecolor='green', alpha=0.5)
                st.pyplot(fig)
            else:
                st.write('*The class distribution in this columns*')
                for p in percent:
                    st.dataframe(p,500,400)
                cnt=df[b].value_counts().to_frame()
                fig, ax = plt.subplots()
                ax.bar(list(cnt.index),cnt[b],facecolor='green')
                st.pyplot(fig)
                st.write('Bar plot of this column')
    os.remove("df")
    os.remove("bias")
    os.remove("percent")

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

    feat_importances = pd.Series(model.feature_importances_, index=x_.columns)

    st.header("Feature Importance")
    st.bar_chart(feat_importances)

elif option == "Try the bias checker":# This is the main page of the app
    
    

    st.write("""
        ### Please upload the csv file you want to check bias for. 
    """)
    
    multiple_files = st.file_uploader('Enter a csv file',type=["csv"])
    
    

    if multiple_files!=None:
        text = st.text_input("Please provide name of target variable column")
        if st.button("Submit"):
            try:
                df_=pd.read_csv(multiple_files)
                df =df_
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
                                cnt=df[b].value_counts().to_frame()
                                fig, ax = plt.subplots()
                                ax.bar(list(cnt.index),cnt[b],facecolor='green')
                                st.pyplot(fig)
                                st.write('Bar plot of this column')
                        st.write('*class distributions*')
                        for p in percent:
                            st.dataframe(p,500,400)
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
                    y = df[text].to_numpy()
                    collist = df.columns.tolist()
                    collist.remove(text)
                    x_ = df[collist]
                    x = df[collist].to_numpy()

                    model = ExtraTreesClassifier()
                    model.fit(x,y)

                    feat_importances = pd.Series(model.feature_importances_, index=x_.columns)
                
                    st.header("Feature Importance")
                    st.bar_chart(feat_importances)
                    
                
                except Exception as e:
                    st.write(e)
            except Exception as e:
                st.write("Please upload file")
        else:
            st.write("Please provide target variable name")
    else:
        st.write("Please Provide a csv file")