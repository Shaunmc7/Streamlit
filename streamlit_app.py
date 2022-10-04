#imports
import streamlit as st
import streamlit.components.v1 as components
import pydeck as pdk
import numpy as np
import pandas as pd 
from functools import reduce
import altair as alt

#Config
alt.renderers.set_embed_options(theme='dark')

# page config

st.set_page_config(page_title='HR dashboard',
                    page_icon="🌳",
                    layout='wide'
)

st.title("Information about our HR data set")

#Importing the dataset and starting EDA
@st.experimental_singleton
def load_data():
    manager_survey = pd.read_csv('manager_survey_data.csv',  sep = ',')
    general_data = pd.read_csv('general_data.csv',  sep = ',')
    employee_data = pd.read_csv('employee_survey_data.csv',  sep = ',')
    emp_man = pd.merge(manager_survey, employee_data, on='EmployeeID')
    data_hr = pd.merge(emp_man, general_data, on='EmployeeID')
    return data_hr
    data_hr = load_data()

data_hr.dropna(inplace=True)
data_hr.drop(['Over18', 'EmployeeCount', 'StandardHours'], inplace=True, axis=1)

data_hr = data_hr.astype({'EnvironmentSatisfaction':'int64','JobSatisfaction':'int64','WorkLifeBalance':'int64','NumCompaniesWorked':'int64'})
data_hr['Attrition'] = data_hr['Attrition'].replace(['Yes'],True)
data_hr['Attrition'] = data_hr['Attrition'].replace(['No'],False)