import streamlit as st
import joblib
import pandas as pd


style ="""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: rgb(2,189,233);
        background: linear-gradient(148deg, rgba(2,189,233,1) 0%, rgba(178,251,37,1) 59%, rgba(2,189,233,1) 100%);
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

st.title("Energy Consumption Prediction")

# Load the trained models
rf_regressor = joblib.load('random_forest_regressor.pkl')
svr_regressor = joblib.load('support_vector_regressor.pkl')

# Define the input form
def input_form():
    st.write("Enter the following information to predict energy consumption:")
    Weather_Temperature = st.number_input("Weather Temperature", min_value=0.0, max_value=100.0, step=0.1)
    Weather_Humidity = st.number_input("Weather Humidity", min_value=0.0, max_value=100.0, step=0.1)
    Weather_Precipitation = st.number_input("Weather Precipitation", min_value=0.0, max_value=100.0, step=0.1)
    Weather_Wind_Speed = st.number_input("Weather Wind Speed", min_value=0.0, max_value=100.0, step=0.1)
    Weather_Solar_Radiation = st.number_input("Weather Solar Radiation", min_value=0.0, max_value=1000.0, step=1.0)
    Building_Size = st.number_input("Building Size", min_value=0, step=1)
    Building_Age = st.number_input("Building Age", min_value=0, step=1)
    Occupancy_Count = st.number_input("Occupancy Count", min_value=0, step=1)
    Equipment_Usage_HVAC = st.number_input("Equipment Usage HVAC", min_value=0, step=1)
    Equipment_Usage_Lighting = st.number_input("Equipment Usage Lighting", min_value=0, step=1)
    Equipment_Usage_Machinery = st.number_input("Equipment Usage Machinery", min_value=0, step=1)
    Electricity_Price = st.number_input("Electricity Price", min_value=0.0, step=0.01)
    Gas_Price = st.number_input("Gas Price", min_value=0.0, step=0.01)
    
    if st.button("Predict"):
        input_data = {
            "Weather_Temperature": Weather_Temperature,
            "Weather_Humidity": Weather_Humidity,
            "Weather_Precipitation": Weather_Precipitation,
            "Weather_Wind_Speed": Weather_Wind_Speed,
            "Weather_Solar_Radiation": Weather_Solar_Radiation,
            "Building_Size": Building_Size,
            "Building_Age": Building_Age,
            "Occupancy_Count": Occupancy_Count,
            "Equipment_Usage_HVAC": Equipment_Usage_HVAC,
            "Equipment_Usage_Lighting": Equipment_Usage_Lighting,
            "Equipment_Usage_Machinery": Equipment_Usage_Machinery,
            "Electricity_Price": Electricity_Price,
            "Gas_Price": Gas_Price
        }
        
        prediction_rf = rf_regressor.predict(pd.DataFrame([input_data]))
        prediction_svr = svr_regressor.predict(pd.DataFrame([input_data]))
        
        st.write("Random Forest Prediction:", prediction_rf[0])
        st.write("Support Vector Regression Prediction:", prediction_svr[0])

# Run the Streamlit app
if __name__ == "__main__":
    input_form()
