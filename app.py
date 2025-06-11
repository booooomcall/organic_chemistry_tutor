import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

with open("assets/styles.css") as f:
    st.markdown('<div class="custom-header">🧪 Organic Chemistry Tutor</div>', unsafe_allow_html=True)


st.title("🧪 Organic Chemistry Tutor")
st.write("Use the sidebar to explore the chemistry topics 📚")
