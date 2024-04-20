import streamlit as st
import os
from deta import Deta

# Initialize Deta Base
DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
deta = Deta(DETA_KEY)
my_db = deta.Base("SayReport")

style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: rgb(233,195,2);
        background: linear-gradient(148deg, rgba(233,195,2,1) 0%, rgba(250,255,0,1) 37%, rgba(254,255,0,1) 64%, rgba(233,195,2,1) 100%);
    }
    
    h1{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 40px;
        color: #8e4305;
    }
    
    p{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #8e4305;
    }
    
    h2{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 30px;
        color: #8e4305;
    }
    
    h3{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 30px;
        color: #8e4305;
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

st.markdown(style, unsafe_allow_html=True)

uploads = "C:/Users/sharm/OneDrive/Desktop/Envdata/uploads"

# Function to save uploaded images
def save_uploaded_image(uploaded_image):
    with open(os.path.join("uploads", uploaded_image.name), "wb") as f:
        f.write(uploaded_image.getbuffer())
    return st.success("Image saved successfully!")

# Main content
st.title("Report Unmaintained Locations")

# Allow user to input email and username
email = st.text_input("Enter your email:")
username = st.text_input("Enter your username:")

# Allow user to upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# If an image is uploaded, display it and save it to local machine
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    save_uploaded_image(uploaded_image)

# Button to submit the report
if st.button("Submit Report"):
    # Save the email and username to Deta Base
    my_db.put({"email": email, "username": username})
    st.success("Report submitted successfully!")
