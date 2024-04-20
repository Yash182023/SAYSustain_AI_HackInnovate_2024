import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.colors as pc



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
        font-size: 40px;
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
# Load the climate change data
df = pd.read_csv("climate_change.csv")
# Set the title of the Streamlit app
st.title("Climate Change Dashboard")

# Display the dataset
st.subheader("Climate Change Data")
st.write(df)

# Create bar charts
st.subheader("Bar Charts")

# Temperature anomaly over the years
fig_temp = px.bar(df, x="Year", y="Temperature_Anomaly_Degrees_Celsius", 
                  title="Temperature Anomaly (°C) Over the Years",
                  color_discrete_sequence=["#FF5733"])  # Custom color
st.plotly_chart(fig_temp)

# Precipitation anomaly over the years
fig_precip = px.bar(df, x="Year", y="Precipitation_Anomaly_mm", 
                    title="Precipitation Anomaly (mm) Over the Years",
                    color_discrete_sequence=["#33FF57"])  # Custom color
st.plotly_chart(fig_precip)

# Create histograms
st.subheader("Histograms")

# Histogram of Sea Level Rise
fig_sea_level = px.histogram(df, x="Sea_Level_Rise_mm", 
                              title="Distribution of Sea Level Rise (mm)",
                              color_discrete_sequence=["#3366FF"])  # Custom color
st.plotly_chart(fig_sea_level)

# Histogram of CO2 Concentration
fig_co2_concentration = px.histogram(df, x="CO2_Concentration_ppm", 
                                     title="Distribution of CO2 Concentration (ppm)",
                                     color_discrete_sequence=["#FF33FF"])  # Custom color
st.plotly_chart(fig_co2_concentration)

# Histogram of Glacier Mass Balance
fig_glacier_mass_balance = px.histogram(df, x="Glacier_Mass_Balance_mm", 
                                        title="Distribution of Glacier Mass Balance (mm)",
                                        color_discrete_sequence=["#FFFF33"])  # Custom color
st.plotly_chart(fig_glacier_mass_balance)