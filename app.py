import streamlit as st
from models.predictor import train_model

model = train_model()

st.title("AI Health Risk Predictor")

sleep = st.slider("Sleep Hours",0,12)
activity = st.slider("Activity Level",0,10)
heart_rate = st.slider("Heart Rate",60,120)

if st.button("Predict"):

    result = model.predict([[sleep,activity,heart_rate]])

    if result[0] == 1:
        st.error("High Health Risk")
    else:
        st.success("Low Health Risk")