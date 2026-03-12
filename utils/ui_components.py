import streamlit as st

def load_css():
    st.markdown("""
    <style>

    .stApp {
        background-color:#0f172a;
        color:white;
    }

    .title {
        font-size:40px;
        font-weight:bold;
        text-align:center;
        color:#38bdf8;
    }

    .subtitle {
        text-align:center;
        color:#94a3b8;
    }

    </style>
    """, unsafe_allow_html=True)