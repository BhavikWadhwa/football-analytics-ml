# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("models/match_predictor.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

st.set_page_config(page_title="Canada West Match Predictor", page_icon="⚽")

st.title("⚽ Canada West Soccer Match Predictor")
st.markdown("Predict match outcomes between any two teams based on 2025-26 season data.")

# Load team names from encoder
teams = sorted(label_encoder.classes_)

# Select teams
home_team = st.selectbox("🏠 Home Team", teams)
away_team = st.selectbox("🚗 Away Team", [t for t in teams if t != home_team])

if st.button("Predict Result"):
    # Encode teams
    home_enc = label_encoder.transform([home_team])[0]
    away_enc = label_encoder.transform([away_team])[0]

    # Predict
    pred = model.predict([[home_enc, away_enc]])[0]
    probs = model.predict_proba([[home_enc, away_enc]])[0]

    st.subheader(f"📊 Prediction: **{pred.replace('_', ' ').title()}**")
    st.write("Confidence:")
    st.write({
        "Home Win": f"{probs[list(model.classes_).index('home_win')]*100:.1f}%",
        "Draw": f"{probs[list(model.classes_).index('draw')]*100:.1f}%",
        "Away Win": f"{probs[list(model.classes_).index('away_win')]*100:.1f}%"
    })

st.markdown("---")
st.caption("Model trained on Canada West 2025-26 match data (Logistic Regression).")
