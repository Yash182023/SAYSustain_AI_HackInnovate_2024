import streamlit as st
import pandas as pd
import plotly.express as px

style ="""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: rgb(2,189,233);
        background: linear-gradient(148deg, rgba(2,189,233,1) 0%, rgba(126,37,251,1) 59%, rgba(2,189,233,1) 100%);
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
st.title('Biodiversity Data Dashboard')

# Sidebar for filtering options
st.sidebar.subheader('Filter Data')
location_filter = st.sidebar.multiselect('Select Locations', df['Location'].unique())

# Filter data based on selected filters
filtered_df = df[df['Location'].isin(location_filter)]

# Define color palette
colors = px.colors.qualitative.Pastel

# Pie chart for Green Space (%)
st.subheader('Green Space (%)')
green_space_fig = px.pie(filtered_df, values='Green_Space(%)', names='Location',
                         title='Green Space (%) by Location', color='Location',
                         color_discrete_sequence=colors)
st.plotly_chart(green_space_fig)

# Pie chart for Biodiversity Index
st.subheader('Biodiversity Index')
biodiversity_fig = px.pie(filtered_df, values='Biodiversity_Index', names='Location',
                          title='Biodiversity Index by Location', color='Location',
                          color_discrete_sequence=colors)
st.plotly_chart(biodiversity_fig)

# Pie chart for Species Abundance
st.subheader('Species Abundance')
species_abundance_fig = px.pie(filtered_df, values='Species_Abundance', names='Location',
                               title='Species Abundance by Location', color='Location',
                               color_discrete_sequence=colors)
st.plotly_chart(species_abundance_fig)
