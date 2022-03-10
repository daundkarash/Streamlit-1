import streamlit as st
import pandas as pd
import numpy as np
import time

data = pd.read_csv("data//ETL-ELT Tool Accelerator_Finalized.xlsx - Detail Score.csv")
 
# st.dataframe(data)

st.dataframe(data, width=2000, height=900)

@st.cache
def ret_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time())

if st.checkbox("2"):
    st.write(ret_time())