import streamlit as st
import pandas as pd
import plotly.express as px

style ="""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: rgb(105,199,255);
        background: linear-gradient(148deg, rgba(105,199,255,1) 0%, rgba(34,5,122,1) 49%, rgba(9,181,176,1) 100%);
    }
    
    h1{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 40px;
        color: #ffffff;
    }
    
    p{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #ffffff;
        
    }
    h2{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 30px;
        color: #ffffff;
    }
    
    h3{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 30px;
        color: #ffffff;
    }
    
    .st-emotion-cache-6qob1r{
        position: relative;
        height: 100%;
        width: 100%;
        overflow: overlay;
        background: rgb(252,0,94);
        background: linear-gradient(164deg, rgba(252,0,94,1) 0%, rgba(89,1,72,1) 100%);
    }
</style>
"""
st.markdown(style,unsafe_allow_html=True)

# Load the environmental data CSV
df = pd.read_csv('environmental_data_new.csv')

# Define Streamlit app
st.title('Air Quality Dashboard')

# Sidebar for filtering options
st.sidebar.subheader('Filter Data')
location_filter = st.sidebar.multiselect('Select Locations', df['Location'].unique())

# Filter data based on selected filters
filtered_df = df[df['Location'].isin(location_filter)]

# Define color palette
colors = px.colors.qualitative.Pastel

# Bar plot for AQI
st.subheader('Air Quality Index (AQI)')
aqi_fig = px.bar(filtered_df, x='Location', y='AQI', 
                 title='Air Quality Index (AQI) by Location', color='Location', 
                 color_discrete_sequence=colors)
st.plotly_chart(aqi_fig)
