import streamlit as st
import joblib

# Load the trained model pipeline
model = joblib.load("models/spam_model.pkl")

# Streamlit UI
st.set_page_config(page_title="Spam Mail Detector", layout="centered")
st.title("📧 Spam Mail Detector")
st.write("Paste any email text below and the model will predict whether it's **Spam** or **Not Spam**.")

# Input
email_text = st.text_area("✉️ Email Content", height=200)

# Prediction
if st.button("🔍 Analyze"):
    if not email_text.strip():
        st.warning("Please enter some email content first.")
    else:
        prediction = model.predict([email_text])[0]
        if prediction == 1:
            st.error("❌ This email is likely **SPAM**.")
        else:
            st.success("✅ This email is **NOT SPAM**.")
