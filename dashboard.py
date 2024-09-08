import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Malaysia Vet Services", page_icon=":dog:", layout="wide")

st.title(":dog::cat: Malaysia Vet Services 2021")
st.markdown('<style>div.block-container{padding-top:3rem}</style>', unsafe_allow_html=True)

# URL to raw CSV file in your GitHub repo
url = "https://raw.githubusercontent.com/oishylea/MalaysiaVetServices/main/updatedRegisteredVet.csv"
df = pd.read_csv(url, encoding="ISO-8859-1")

# Side bar

# Region
st.sidebar.header("Choose filter:")
negeri = st.sidebar.multiselect("Pick state", df["Negeri"].unique())

if not negeri:
    df2 = df.copy()
else:
    df2 = df[df["Negeri"].isin(negeri)]

# Create for state

daerah = st.sidebar.multiselect("Pick district", df2["Daerah"].unique())
if not daerah:
    df3 = df2.copy()
else:
    df3 = df2[df2["Daerah"].isin(daerah)]

# Filter data based on state, district
if not negeri and not daerah:
    filtered_df = df
elif not negeri:
    filtered_df = df[df["Daerah"].isin(daerah)]
elif not daerah:
    filtered_df = df[df["Negeri"].isin(negeri)]
elif negeri and daerah:
    filtered_df = df3[df["Negeri"].isin(negeri) & df3["Daerah"].isin(daerah)]
else:
    filtered_df = df3[df3["Negeri"].isin(negeri) & df3["Daerah"].isin(daerah)]

# Count frequency of each "Negeri"
frequency_by_negeri = filtered_df['Negeri'].value_counts().reset_index()
frequency_by_negeri.columns = ['Negeri', 'Frequency']

# Display the frequency counts
cl1, cl2 = st.columns(2)
with cl1:
    st.subheader("Frequency by State")
    
    # Define soft colors for each state
    soft_colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D3B9E0', '#D4E157', '#A8E6CE', '#FFD54F', '#FFB74D', '#FF8C94']
    
    # Create a color mapping for each unique 'Negeri'
    unique_negeri = frequency_by_negeri['Negeri'].unique()
    color_map = {negeri: soft_colors[i % len(soft_colors)] for i, negeri in enumerate(unique_negeri)}
    
    # Map colors to the DataFrame
    frequency_by_negeri['Color'] = frequency_by_negeri['Negeri'].map(color_map)

    # Create the bar chart
    fig = px.bar(
        frequency_by_negeri,
        x="Negeri",
        y="Frequency",
        text='Frequency',
        color='Color',  # Use the mapped color
        template="seaborn",
        color_discrete_sequence=frequency_by_negeri['Color']  # Set colors
    )
    
    # Rename the axes
    fig.update_layout(
        xaxis_title="State",
        yaxis_title="Frequency"
    )
    
    st.plotly_chart(fig, use_container_width=True)

with cl2:
    st.subheader("Detailed View")
    st.write(frequency_by_negeri)
