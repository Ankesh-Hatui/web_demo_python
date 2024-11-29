import streamlit as st
import pandas as pd
st.title('Hi , I am Ankesh Hatui')
st.header('I am a Developer and Designer')
st.subheader('Code')
st.markdown('Python')
dataset=pd.read_csv('carprices.csv')
st.dataframe(dataset)

name=st.text_input('Enter Your Name: ')
parent=st.text_input('Enter your parent Name: ')

address=st.text_area('Enter your address: ')
year=st.selectbox('Enter date of birth',(2018,2019,2020,2021,2022,2023))

button=st.button('Submit')

if button:

    st.markdown(f"""

        Name= {name} ,
        parent={parent},
        address= {address},
        DOB= {year}

""")