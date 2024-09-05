import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Malaysia Vet Services", page_icon=":dog:", layout="wide")

st.title(":dog::cat: Malaysia Vet Services 2021")
st.markdown('<style>div.block-container{padding-top:3rem}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(fl, encoding="ISO-8859-1")
else:
    # URL to raw CSV file in your GitHub repo
    url = "https://raw.githubusercontent.com/oishylea/MalaysiaVetServices/main/updatedRegisteredVet.csv"
    df = pd.read_csv(url, encoding="ISO-8859-1")

# Side bar

# Region
st.sidebar.header("Choose filter:")
negeri = st.sidebar.multiselect("Pick region", df["Negeri"].unique())

if not negeri:
    df2 = df.copy()
else:
    df2 = df[df["Negeri"].isin(negeri)]

# Create for state

daerah = st.sidebar.multiselect("Pick state", df2["Daerah"].unique())
if not daerah:
    df3 = df2.copy()
else:
    df3 = df2[df2["Daerah"].isin(daerah)]