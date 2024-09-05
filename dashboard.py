import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Malaysia Vet Services 2021", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Malaysia Vet Services")
st.markdown('<style>div.block-container{padding-top:2rem}</style>', unsafe_allow_html=True)
