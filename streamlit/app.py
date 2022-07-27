from matplotlib.pyplot import step
from numpy import result_type
import streamlit as st
import requests
from PIL import Image

# diabetes explanation
st.title("Customer Churn Prediction")
st.title('           ')
st.subheader('What is Churn ?')
st.markdown('Churn is a measurement of the percentage of accounts that cancel or choose not to renew their subscriptions. A high churn rate can negatively impact Monthly Recurring Revenue (MRR) and can also indicate dissatisfaction with a product or service.') 
st.title('           ')
img = Image.open('image6.png')
st.image(img, width=400, use_column_width=True)
st.title('           ')
st.markdown('Churn is the measure of how many customers stop using a product. This can be measured based on actual usage or failure to renew (when the product is sold using a subscription model). Often evaluated for a specific period of time, there can be a monthly, quarterly, or annual churn rate.') 
st.subheader('Dataset Information !!')
st.header('           ')
st.markdown('The data set includes information about:')
st.markdown('- Customers who left within the last month => the column is called Churn')
st.markdown('- Services that each customer has signed up for => phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies')
st.markdown('- Customer account information => how long they been a customer, contract, payment method, paperless billing, monthly charges, and total charges')
st.markdown('- Demographic info about customers => gender, age range, and if they have partners and dependents')
st.header('           ')
st.subheader('Check Customer !!')

# Telco Customer Churn Database
# Predict the churn
tenure = st.number_input("Tenure")
totalcharges = st.number_input("Total Charges")
monthlycharges = st.number_input("Monthly Charges")
contract = st.selectbox("Contract", ["Month to month", "One year", "Two year"])
online_security = st.selectbox("Online Security", ["No", "No internet service", "Yes"])
techsupport = st.selectbox("Tech Support", ["No", "No internet service", "Yes"])
onlinebackup = st.selectbox("Online Backup", ["No", "No internet service", "Yes"])
deviceprotection = st.selectbox("Device Protection", ["No", "No internet service", "Yes"])
seniorcitizen= st.selectbox("Senior Citizen", [0, 1])
dependents = st.selectbox("Dependents", ["No", "Yes"])
paperlessbilling = st.selectbox("Paperless Billing", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
submit = st.button('Predict')

# inference
data = { "tenure" : tenure,
        "totalcharges" : totalcharges,
        "monthlycharges" : monthlycharges,
        "contract" : contract,
        "online_security" : online_security,
        "techsupport" : techsupport,
        "onlinebackup" : onlinebackup,
        "deviceprotection" : deviceprotection,
        "seniorcitizen" : seniorcitizen,
        "dependents" : dependents,
        "paperlessbilling" : paperlessbilling,
        "partner" : partner}

# communication
if submit:
    URL = "https://backend-churn-ilmi.herokuapp.com/v1/models/churn:predict" 
    r = requests.post(URL, json=data)
    res = r.json()
    prediction =  {'predictions': [[0], [0], [0]]}
    if prediction == 0.5:
        st.write("This customer will churn!!!")
    else:
        st.write("This customer will stay with company!!!")
