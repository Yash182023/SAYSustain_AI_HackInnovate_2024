import streamlit as st
import pandas as pd
import plotly.express as px

style ="""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: rgb(240,255,131);
        background: linear-gradient(148deg, rgba(240,255,131,1) 0%, rgba(255,191,253,1) 60%, rgba(98,249,255,1) 100%);
    }
    
    h1{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 40px;
        color: #6c1b09;
    }
    
    p{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #6c1b09;
    }
    
    h2{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 30px;
        color: #6c1b09;
    }
    
    h3{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 30px;
        color: #6c1b09;
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
# Load the data from the CSV file

st.title("Industry Locations of different cities")
df = pd.read_csv("industry_locations_cities.csv")

st.write("Dataset we are using")
# Display the DataFrame
st.write(df)

# Create a Plotly map
fig = px.scatter_mapbox(df, 
                        lat="Latitude", 
                        lon="Longitude", 
                        hover_name="Location Name",
                        hover_data=["Description", "Industry Type", "Demographic Information", "Environmental Factors"],
                        zoom=3)

# Customize the map layout
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.write("Locate the best place")
# Show the map
st.plotly_chart(fig)
