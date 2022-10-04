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
    'Select Department',
    ('Human Resources', 'Research & Development', 'Sales'))

st.write('You selected:', option)

filtered_df = AttritionFalse[AttritionFalse['Department'] == option]

filtered_df['AgeGroups'] = pd.cut(filtered_df['Age'], bins=[18, 25, 30, 40, 50, 60, 70, np.inf], include_lowest=True)
filtered_df['IncomeGroups'] = pd.cut(filtered_df['MonthlyIncome'], bins=[10000, 25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, np.inf])
filtered_df['YearsAtCompanyGroups'] = pd.cut(filtered_df['YearsAtCompany'], bins=[-1, 2, 5, 10, 15, 20, 30, 40, np.inf])

#Gender
st.subheader("Gender")
Gender_chart = pd.crosstab(filtered_df.Gender, filtered_df.Gender.count())
st.bar_chart(Gender_chart)

col1, col2 = st.columns([1, 1])

#Job Satisfaction
with col1:
    st.subheader("Employee satisfaction")
    st.caption("1 = Low, 2 = Medium, 3 = High, 4 = Very High")
    Satisfaction_chart = pd.crosstab(filtered_df.JobSatisfaction, filtered_df.JobSatisfaction.count())
    st.bar_chart(Satisfaction_chart)

    st.subheader("Education level")
    st.caption("1 = Below College, 2 = College, 3 = Bachelor, 4 = Master, 5 = Doctor")
    Education = pd.crosstab(filtered_df.Education, filtered_df.Education.count())
    st.bar_chart(Education)

    st.subheader("Training sessions last year")
    Training_chart = pd.crosstab(filtered_df.TrainingTimesLastYear, filtered_df.TrainingTimesLastYear.count())
    st.bar_chart(Training_chart)

with col2:
    st.subheader("Work life balance")
    st.caption("1 = Bad, 2 = Good, 3 = Better, 4 = Best")
    WorkLife_chart = pd.crosstab(filtered_df.WorkLifeBalance, filtered_df.WorkLifeBalance.count())
    st.bar_chart(WorkLife_chart)

    st.subheader("Employee field of education")
    education_chart = pd.crosstab(filtered_df.EducationField, filtered_df.EducationField.count())
    st.bar_chart(education_chart)

    st.subheader("Environment satisfaction")
    st.caption("1 = Low, 2 = Medium, 3 = High, 4 = Very High")
    Education = pd.crosstab(filtered_df.EnvironmentSatisfaction, filtered_df.EnviornmentSatifaction.count())
    st.bar_chart(Education)

st.subheader("Job role")
Role_chart = pd.crosstab(filtered_df.JobRole, filtered_df.JobRole.count())
st.bar_chart(Role_chart)

# #Age Plot

# Age_chart = pd.crosstab(filtered_df.AgeGroups, filtered_df.AgeGroups.count())
# st.bar_chart(Age_chart)

# #Income Plot

# Income_chart = pd.crosstab(filtered_df.IncomeGroups, filtered_df.IncomeGroups.count())
# st.bar_chart(Income_chart)

# #Years At Company Plot

# YearsWorked_chart = pd.crosstab(filtered_df.YearsAtCompanyGroups, filtered_df.YearsAtCompanyGroups.count())
# st.bar_chart(YearsWorked_chart)
