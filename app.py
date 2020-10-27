import pandas as pd
import numpy as np
import streamlit as st
import pickle
from os import path
import os
st.title('Bias checker')
multiple_files = st.file_uploader('Enter a csv file',type=["csv"])
df = None
if multiple_files:
    df_=pd.read_csv(multiple_files)
    df =df_
if df is not None:
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
        

