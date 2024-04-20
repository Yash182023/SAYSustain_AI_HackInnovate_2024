import streamlit as st


style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: rgb(105,199,255);
        background: linear-gradient(148deg, rgba(105,199,255,1) 0%, rgba(236,125,182,1) 100%);
    }
    
    h1{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 40px;
        color: #600534;
    }
    
    h2{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #600534;
    }
    p{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #600534;
    }
    
    .st-emotion-cache-6qob1r{
        position: relative;
        height: 100%;
        width: 100%;
        overflow: overlay;
        background: rgb(252,0,94);
        background: linear-gradient(164deg, rgba(252,0,94,1) 0%, rgba(89,1,72,1) 100%);
    }
    
    .st-emotion-cache-1avcm0n{
        background: rgb(0,0,89);
background: linear-gradient(164deg, rgba(0,0,89,1) 16%, rgba(0,150,162,1) 100%, rgba(0,255,136,1) 100%);
    }
</style>

"""

st.markdown(style,unsafe_allow_html=True)

# Page Title
st.title("Sustainability Education")

# Introduction
st.write("""
Welcome to our Sustainability Education page! Here, you can explore various topics related to sustainability and learn how you can contribute to a greener future.
""")

# Section 1: What is Sustainability?
st.header("What is Sustainability?")
st.write("""
Sustainability is the practice of meeting the needs of the present without compromising the ability of future generations to meet their own needs. It encompasses environmental, social, and economic aspects and aims to create a balance between these pillars for a harmonious coexistence with nature.
""")

# Section 2: Why is Sustainability Important?
st.header("Why is Sustainability Important?")
st.write("""
Sustainability is crucial for addressing pressing global challenges such as climate change, biodiversity loss, and resource depletion. By adopting sustainable practices, we can mitigate the impacts of these challenges and create a more resilient and equitable world for current and future generations.
""")

# Section 3: Sustainable Practices
st.header("Sustainable Practices")
st.write("""
There are many ways individuals and organizations can incorporate sustainability into their daily lives and operations. Here are some sustainable practices you can adopt:
- Reduce, Reuse, Recycle
- Conserve Energy and Water
- Support Renewable Energy Sources
- Choose Sustainable Transportation Options
- Eat Locally Sourced and Organic Food
- Reduce Waste and Plastic Usage
- Advocate for Sustainable Policies and Practices
""")

# Section 6: Additional Resources
st.header("Additional Resources")
st.write("""
Explore the following resources to learn more about sustainability:
- [United Nations Sustainable Development Goals](https://sdgs.un.org/)
- [World Wildlife Fund (WWF) - Living Planet Report](https://www.worldwildlife.org/pages/living-planet-report-2020)
- [The Nature Conservancy - Conservation Initiatives](https://www.nature.org/en-us/what-we-do/our-insights/perspectives/)
- [Environmental Protection Agency (EPA) - Sustainability Resources](https://www.epa.gov/sustainability)
""")

st.subheader("What is sustainability?")
url1 = "https://www.youtube.com/watch?v=zx04Kl8y4dE&ab_channel=UCLA"# Replace with your YouTube video URL or ID
st.video(url1)
st.subheader("Listen the TED_TeLK")
url2 = "https://www.youtube.com/watch?v=B-dCmbViDEQ&ab_channel=TEDxTalks"
st.video(url2)
# Footer
st.write("""
Thank you for exploring our Sustainability Education page. Together, let's work towards a sustainable future!
""")
