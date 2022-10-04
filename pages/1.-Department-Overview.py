#imports
import streamlit as st
import streamlit.components.v1 as components
import pydeck as pdk
import numpy as np
import pandas as pd 
from functools import reduce
import altair as alt

st.title("Department Overview")

#Loading data
@st.experimental_singleton
def load_data():
    manager_survey = pd.read_csv('manager_survey_data.csv',  sep = ',')
    return manager_survey

manager_survey = load_data()

@st.experimental_singleton
def load_data():
    general_data = pd.read_csv('general_data.csv',  sep = ',')
    return general_data

general_data = load_data()

@st.experimental_singleton
def load_data():
    employee_data = pd.read_csv('employee_survey_data.csv',  sep = ',')
    return employee_data

employee_data = load_data()

emp_man = pd.merge(manager_survey, employee_data, on='EmployeeID')
data_hr = pd.merge(emp_man, general_data, on='EmployeeID')

data_hr.dropna(inplace=True)
data_hr.drop(['Over18', 'EmployeeCount', 'StandardHours'], inplace=True, axis=1)

data_hr = data_hr.astype({'EnvironmentSatisfaction':'int64','JobSatisfaction':'int64','WorkLifeBalance':'int64','NumCompaniesWorked':'int64'})
data_hr['Attrition'] = data_hr['Attrition'].replace(['Yes'],True)
data_hr['Attrition'] = data_hr['Attrition'].replace(['No'],False)
AttritionFalse = data_hr[data_hr.Attrition == False]

data_hr['AgeGroups'] = pd.cut(data_hr['Age'], bins=[18, 25, 30, 40, 50, 60, 70, np.inf], include_lowest=True)
data_hr['IncomeGroups'] = pd.cut(data_hr['MonthlyIncome'], bins=[10000, 25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, np.inf])
data_hr['YearsAtCompanyGroups'] = pd.cut(data_hr['YearsAtCompany'], bins=[-1, 2, 5, 10, 15, 20, 30, 40, np.inf])

#Select box

option = st.selectbox(
    'Department',
    ('Human Resources', 'Research & Development', 'Sales'))

st.write('You selected:', option)

filtered_df = AttritionFalse[AttritionFalse['Department'] == option]

#Education Plot

education_chart = pd.crosstab(filtered_df.EducationField, filtered_df.EducationField.count())
st.bar_chart(education_chart)

#Training Plot

Training_chart = pd.crosstab(filtered_df.TrainingTimesLastYear, filtered_df.TrainingTimesLastYear.count())
st.bar_chart(Training_chart)

#Age Plot

Age_chart = pd.crosstab(filtered_df.Age, filtered_df.Age.count())
st.line_chart(Age_chart)

#Income Plot

Income_chart = pd.crosstab(filtered_df.IncomeGroups, filtered_df.IncomeGroups.count())
st.bar_chart(Income_chart)

#Years At Company Plot

YearsWorked_chart = pd.crosstab(filtered_df.YearsAtCompanyGroups, filtered_df.YearsAtCompanyGroups.count())
st.bar_chart(YearsWorked_chart)
