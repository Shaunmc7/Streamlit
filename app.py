# Load packages (comments for more special stuff)

import pandas as pd
import pickle # un-pickling stuff from training notebook
from xgboost import XGBClassifier # we use a trained XGBoost model...and therefore need to load it
from sklearn.preprocessing import StandardScaler
import shap # add prediction explainability

import numpy as np
import itertools # we need that to flatten ohe.categories_ into one list for columns
import streamlit as st
from streamlit_shap import st_shap # wrapper to display nice shap viz in the app

#this is how you can add images e.g. from unsplash (or loca image file)

# use this decorator (--> @st.experimental_singleton) and 0-parameters function to only load and preprocess once
@st.experimental_singleton
def read_objects():
    model_xgb = pickle.load(open('model_xgb.pkl','rb'))
    scaler = pickle.load(open('scaler.pkl','rb'))
    selected_sml_df = pickle.load(open('selected_sml_df.pkl','rb'))
    shap_values = pickle.load(open('shap_values.pkl','rb'))
    return model_xgb, scaler, selected_sml_df, shap_values

model_xgb, scaler, selected_sml_df, shap_values = read_objects()






#Features
Age = st.number_input("Insert Age Of Employee",min_value=1, max_value=999)
JobSatisfaction = st.number_input("Insert JobSatisfaction",min_value=1, max_value=999)
TotalWorkingYears = st.number_input("Total amount of working years",min_value=1, max_value=999)
YearsAtCompany = st.number_input("Amount of years worked at this company", min_value=1, max_value=999)
YearsWithCurrManager = st.number_input("Years worked with the current manager", min_value=1, max_value=999)
EnvironmentSatisfaction = st.number_input("Insert satisfaction with workplace", min_value=1, max_value=999)
#write some markdown blah
# with st.expander("What's that app?"):
#     st.markdown("""
#     The risk of attrition.
#     """)







st.subheader('Result of the SML algorithm')


if st.button('Predict! 🚀'):
  
    new_df_num = pd.DataFrame({'Age': Age, 
                            'JobSatisfaction': JobSatisfaction, 
                            'TotalWorkingYears':TotalWorkingYears, 
                            'YearsAtCompany':YearsAtCompany, 
                            'YearsWithCurrManager':YearsWithCurrManager,
                            'EnvironmentSatisfaction':EnvironmentSatisfaction}, index=[0])



    new_values_num = pd.DataFrame(scaler.transform(new_df_num), columns = new_df_num.columns, index=[0])
    # predicted_value = model_xgb.predict(selected_sml_df.iloc[:1, :6].values )
    predicted_value = model_xgb.predict(new_values_num)[0]

    st.metric(label="Atrrition prediction", value=(predicted_value))
    #st.write(selected_sml_df.iloc[:1, :6].values)
    #st.write(predicted_value)
    #print out result to user
    # st.metric(label="Predict risk of attrition")
    
    #print SHAP explainer to user