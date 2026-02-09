import streamlit as st
import pandas as pd 
import joblib
import os

model_filename = os.path.join("App", "model", "fraud_detection_model.pkl")
with open(model_filename, 'rb') as file:
    model = joblib.load(file)

# =========================
# Page config
# =========================
st.set_page_config(
    page_title="Fraud Detection",
    page_icon="🕵️",
    layout="centered"
)

# =========================
# Dark Fraud Theme CSS
# =========================
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background: linear-gradient(135deg, #020617, #020617);
        color: #e5e7eb;
    }

    /* Titles */
    h1, h2, h3 {
        color: #22c55e;
        text-align: center;
    }

    /* Input boxes */
    input, select {
        background-color: #020617 !important;
        color: #e5e7eb !important;
        border: 1px solid #334155 !important;
        border-radius: 8px;
    }

    /* Labels */
    label {
        color: #cbd5f5 !important;
        font-weight: 600;
    }

    /* Predict button */
    div.stButton > button {
        background: linear-gradient(90deg, #22c55e, #16a34a);
        color: black;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        border: none;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #16a34a, #22c55e);
        transform: scale(1.02);
    }

    /* Success message */
    .stAlert.success {
        background-color: #052e16;
        border-left: 6px solid #22c55e;
        color: #bbf7d0;
    }

    /* Error message */
    .stAlert.error {
        background-color: #450a0a;
        border-left: 6px solid #ef4444;
        color: #fecaca;
    }

    /* Divider */
    hr {
        border: 1px solid #1e293b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🕵️ Fraud Detection System")
st.markdown(
    "<p style='text-align:center; color:#94a3b8;'>"
    "Enter transaction details and detect suspicious behavior"
    "</p>",
    unsafe_allow_html=True
)


st.divider()

transaction_type = st.selectbox("Transaction Type" , ["CASH_OUT" ,"PAYMENT","CASH_IN","TRANSFER","DEPOSIT"])
amount = st.number_input("Amount" , min_value= 0.0 , value=1000.0)

oldbalanceOrg = st.number_input("Old Balance (Sender)" , min_value=0.0,value=10000.0,step=50.0)
newbalanceOrig = st.number_input("New Balance (Sender)" , min_value=0.0,value=9000.0,step=50.0)

oldbalanceDest = st.number_input("Old Balance (Receiver)" , min_value=0.0,value=0.0,step=50.0)
newbalanceDest = st.number_input("New Balance (Receiver)" , min_value=0.0,value=0.0,step=50.0)

st.divider()

if st.button("predict"):
    input_data = pd.DataFrame([
        {
            'type':transaction_type,
            'amount':amount,
            'oldbalanceOrg':oldbalanceOrg,
            'newbalanceOrig':newbalanceOrig,
            'oldbalanceDest':oldbalanceDest,
            'newbalanceDest':newbalanceDest,
            'balanceDiffOrg':oldbalanceOrg -newbalanceOrig,
            'balanceDiffDest':newbalanceDest -oldbalanceDest
        }
    ])

    prediction = model.predict(input_data)[0]
    # st.subheader(f"prediction : '{int(prediction)}'")
    prediction_proba = model.predict_proba(input_data)[0][prediction]
    st.subheader(f"Prediction Probability : '{prediction_proba}'")
    if prediction == 1:
        st.error("This transaction can be Fraud")
    else:
        st.success("This transaction looks like is not Fraud")