import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from auth.auth_ui import auth_page
from auth.auth_db import create_table

from modules.research_nexus import research_page
from modules.coding_nexus import coding_page
from modules.data_nexus import data_page
from modules.image_nexus import image_page
from modules.knowledge_chatbot import chatbot_page

create_table()

st.set_page_config(
    page_title="AI Nexus Studio",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#020617,#0f172a,#020617);
color:white;
}

h1,h2,h3,h4{
color:#38bdf8 !important;
}

label{
color:white !important;
}

.stButton button{
background:#38bdf8;
color:black;
border-radius:10px;
font-weight:600;
height:48px;
}

.stButton button:hover{
background:#0ea5e9;
color:white;
}

section[data-testid="stSidebar"]{
background:#020617;
}

</style>
""", unsafe_allow_html=True)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:

    auth_page()

else:

    with st.sidebar:

        st.markdown("## 🤖 AI Nexus Studio")

        username = st.session_state.email.split("@")[0]
        st.success(f"Welcome {username}")

        st.markdown("---")

        menu = st.selectbox(
            "AI Tools",
            [
                "Research Nexus",
                "Coding Nexus",
                "Data Analysis Nexus",
                "Image Analysis Nexus",
                "Knowledge Chatbot",
            ]
        )

        st.markdown("<div style='height:60vh'></div>", unsafe_allow_html=True)

        if st.button("Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()


    if menu == "Research Nexus":
        research_page()

    elif menu == "Coding Nexus":
        coding_page()

    elif menu == "Data Analysis Nexus":
        data_page()

    elif menu == "Image Analysis Nexus":
        image_page()

    elif menu == "Knowledge Chatbot":
        chatbot_page()