# command : streamlit run main.py

import pandas as pd
import streamlit as st
from get_frequency import compute_frequency

st.title('Date frequency')

st.markdown(
    '<span><i>Process to Identify the distribution of date column</i></span>',
    unsafe_allow_html=True)
st.text('')
st.text('')
uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file:

  df = pd.read_csv(uploaded_file)


  st.text('')
  column = st.selectbox('Select date column',
                          df.columns.tolist() , key='options')

  st.text('')
  if st.button('Submit', key="submit"):

      return_text = compute_frequency(df[column])
      # import time

      # my_bar = st.progress(0)
      # for percent_complete in range(10):
      #     time.sleep(0.1)
      #     my_bar.progress(percent_complete + 1)

      st.markdown(
          '<b> Frequency: </b>' + '<span style="color:green; font-size:16px" >' + return_text + '</span>',
          unsafe_allow_html=True)
