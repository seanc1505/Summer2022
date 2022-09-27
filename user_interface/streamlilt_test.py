import streamlit as st
import pandas as pd

df = pd.read_csv(  "C:/Users/seanc/Documents/0_code/5_Summer2022/test/22_07_04_streamlit_test.csv")

st.title("Test page of a sample dataset")

st.write("Here is the dataset sample:") 

st.write(df)