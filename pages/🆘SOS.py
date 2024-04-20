from twilio.rest import Client
import streamlit as st 

custom_style = """
<style>
    .main {
       background: rgb(255,52,2);
       background: linear-gradient(148deg, rgba(255,52,2,1) 0%, rgba(122,5,96,1) 49%, rgba(2,75,189,1) 100%);
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

    .box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 0 0 5px #690021;
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

st.markdown(custom_style, unsafe_allow_html=True)

# Twilio credentials
account_sid = ''
auth_token = ''
twilio_number = ''
recipient_number = ''  # Update with your recipient's phone number

# Initialize Twilio client
client = Client(account_sid, auth_token)

st.title("Send SOS to Higher Authorities")

cont = """
### Purpose of the SOS Feature:

The SOS feature is designed to provide immediate assistance in emergency situations related to pollution or environmental hazards. Users can activate the SOS to quickly report incidents such as highly polluted areas or other environmental emergencies to the appropriate authorities.

### How to Use:

1. **Activate SOS**: If you encounter a highly polluted area or any environmental emergency, simply press the "SOS - Report Emergency" button to send a distress signal.

2. **Custom Message**: You can enter a custom SOS message to provide additional details about the emergency situation.

3. **Confirmation**: After sending the SOS message successfully, you will receive a confirmation message indicating that the SOS has been sent.

4. **Action Taken**: Authorities will be notified about the emergency, and appropriate action will be taken to address the situation.

Remember, the SOS feature is intended for genuine emergency situations. Please use it responsibly and only in case of actual emergencies.
"""

st.markdown(cont,unsafe_allow_html=True)

def send_sos(message_body):
    try:
        # Send SOS SMS
        message = client.messages.create(
            from_=twilio_number,
            body=message_body,
            to=recipient_number
        )
        return message.sid
    except Exception as e:
        st.error(f"Error sending SOS message: {str(e)}")
        return None

# UI components
message_input = "Attention needed! the area is having high degradation here!"

if st.button("Send SOS"):
    # Send SOS message
    sos_message = message_input.strip()
    if sos_message:
        message_sid = send_sos(sos_message)
        if message_sid:
            st.success("SOS Message sent successfully!")
            st.info(f"SOS Message SID: {message_sid}")
    else:
        st.warning("Please enter a valid SOS message.")
