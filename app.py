import streamlit as st
import os
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

.stApp {
background: linear-gradient(135deg,#020617,#0f172a,#020617);
color:white;
}

/* Headings */
h1,h2,h3,h4,h5 {
color:#38bdf8 !important;
}

/* Labels */
label {
color:white !important;
font-weight:500;
}

/* Text Inputs */
.stTextInput input{
background:#1e293b;
color:white;
}

/* Text Area */
.stTextArea textarea{
background:#1e293b;
color:white;
}

/* Buttons */
.stButton button{
background:#38bdf8;
color:black;
font-weight:600;
border-radius:8px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
background:#020617;
display:flex;
flex-direction:column;
}

/* Sidebar button spacing */
section[data-testid="stSidebar"] button {
margin-top:20px;
}

/* FILE UPLOADER BOX */
[data-testid="stFileUploader"] {
background:white !important;
padding:15px !important;
border-radius:10px !important;
}

/* DRAG AND DROP TEXT */
[data-testid="stFileUploader"] div {
color:black !important;
font-weight:600 !important;
}

/* BROWSE FILE BUTTON */
[data-testid="stFileUploader"] button {
background:#e5e7eb !important;
color:black !important;
font-weight:700 !important;
border-radius:6px !important;
}

/* FORCE BUTTON TEXT BLACK */
[data-testid="stFileUploader"] button span {
color:black !important;
}

/* FILE NAME TEXT */
[data-testid="stFileUploader"] small {
color:black !important;
}

/* Download button text fix */
div[data-testid="stDownloadButton"] button {
color:black !important;
background:white !important;
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

        st.markdown("### AI Tools")

        menu = st.selectbox(
            "",
            [
                "Research Nexus",
                "Coding Nexus",
                "Data Analysis Nexus",
                "Image Analysis Nexus",
                "Knowledge Chatbot",
            ],
        )

        st.markdown(
            """
            <div style="height:55vh;"></div>
            """,
            unsafe_allow_html=True
        )

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