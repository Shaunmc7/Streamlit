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
    New_data = pd.read_csv('New_data.csv',  sep = ',')
    return New_data

New_data = load_data()

AttritionFalse = New_data[New_data.Attrition == False]

#Select box

option = st.selectbox(
    'Select Department',
    ('Human Resources', 'Research & Development', 'Sales'))

st.write('You selected:', option)

filtered_df = AttritionFalse[AttritionFalse['Department'] == option]

#Gender
st.subheader("Gender")
Gender_chart = pd.crosstab(filtered_df.Gender, filtered_df.Gender.count())
st.bar_chart(Gender_chart)

#AGE

st.subheader("Employee age")
age_chart = pd.crosstab(filtered_df.AgeGroups, filtered_df.AgeGroups.count())

st.bar_chart(age_chart)

st.subheader("Employee income")
Income_chart = pd.crosstab(filtered_df.IncomeGroups, filtered_df.IncomeGroups.count())
st.bar_chart(Income_chart)

st.subheader("Years worked at company")
YearsWorked_chart = pd.crosstab(filtered_df.YearsAtCompanyGroups, filtered_df.YearsAtCompanyGroups.count())
st.bar_chart(YearsWorked_chart)

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
    Environment_chart = pd.crosstab(filtered_df.EnvironmentSatisfaction, filtered_df.EnvironmentSatisfaction.count())
    st.bar_chart(Environment_chart)

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
