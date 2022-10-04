#imports
import streamlit as st
import streamlit.components.v1 as components
import pydeck as pdk
import numpy as np
import pandas as pd 
import seaborn as sns 
from functools import reduce
import matplotlib.pyplot as plt
import altair as alt

#Config
alt.renderers.set_embed_options(theme='dark')

# page config

st.set_page_config(page_title='HR Data Analysis',
                    layout='wide'
)

st.title("Information about our HR data set")
