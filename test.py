#imports
import streamlit as st
import streamlit.components.v1 as components
import pydeck as pdk

import numpy as np
import pandas as pd 

import altair as alt
alt.renderers.set_embed_options(theme='dark')

# page config

st.set_page_config(page_title='Streamlit - Dashboard 🤯',
                    page_icon="🚀",
                    layout='wide'
)