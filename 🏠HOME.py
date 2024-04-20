import streamlit as st
import pandas as pd
import plotly.express as px


style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: rgb(131,255,147);
        background: linear-gradient(148deg, rgba(131,255,147,1) 0%, rgba(235,255,191,1) 60%, rgba(180,252,67,1) 100%);
    }
    
    h1{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 40px;
        color: #425f00;
        justify-content: center; /* Horizontal centering */
    }
    
    p{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #425f00;
    }
    
    h2{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 30px;
        color: #425f00;
    }
    
    h3{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 30px;
        color: #425f00;
    }
    
    .st-emotion-cache-6qob1r{
        position: relative;
        height: 100%;
        width: 100%;
        overflow: overlay;
        background: rgb(0,0,89);
background: linear-gradient(164deg, rgba(0,0,89,1) 16%, rgba(0,150,162,1) 100%, rgba(0,255,136,1) 100%);
    }
    
    
</style>
"""

st.markdown(style, unsafe_allow_html=True)


# Define Streamlit app
st.title('SAYSustain_AI')

cont = """
Welcome to the SustainMe_AI, where magic meets sustainability! 
Embark on a mystical journey towards a greener future with our 
AI-driven platform designed to inspire and empower individuals 
and organizations alike. Harnessing the power of enchantment and 
technology, we offer personalized guidance, mystical insights, 
and transformative actions to guide you towards eco-friendly 
practices and green initiatives. Whether you're an individual 
seeking to reduce your carbon footprint or a business striving 
for sustainable growth, our enchanting solutions provide the tools 
and resources you need to make a positive impact on the world 
around you. Join us today and unleash the magic of sustainability!
"""
st.markdown(cont,unsafe_allow_html=True)

# Section: Sustainable Living Tips
st.header("Sustainable Living Tips")
st.write("""
Here are some practical tips for adopting sustainable practices in your daily life:
- **Reduce Waste**: Use reusable bags, containers, and utensils. Compost organic waste.
- **Conserve Energy**: Turn off lights and appliances when not in use. Use energy-efficient light bulbs and appliances.
- **Eco-Friendly Transportation**: Walk, bike, carpool, or use public transportation whenever possible.
""")

# Section: Latest Sustainability News
st.header("Latest Sustainability News")
st.write("""
Stay updated on the latest news and developments in sustainability:
- [GreenBiz](https://www.greenbiz.com/)
- [EcoWatch](https://www.ecowatch.com/)
- [The Guardian - Environment](https://www.theguardian.com/environment)
""")

