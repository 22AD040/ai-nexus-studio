import streamlit as st
from auth.auth_db import register_user, login_user


def auth_page():

    
    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg,#020617,#0f172a,#020617);
        color: white;
    }

    /* Title */
    .title-text {
        text-align:center;
        font-size:150px;
        font-weight:650;
        color:#38bdf8;
        margin-top:10px;
    }

    /* Labels */
    label {
        color: white !important;
        font-size:20px !important;
        font-weight:600;
    }

    /* Login/Register radio bigger */
    .stRadio label {
    font-size:30px !important;
    font-weight:700 !important;
    }

    /* Input fields bigger */
    .stTextInput input {
    height:50px !important;
    font-size:18px !important;
    }

    /* Email + Password input bigger */
    .stTextInput input {
    height:50px !important;
    font-size:18px !important;
    border-radius:8px !important;
    }

    /* Login button bigger */
    .stButton button {
    height:50px !important;
    font-size:18px !important;
    font-weight:600;
    }

    /* Subheaders */
    h3 {
        color:#38bdf8 !important;
        font-weight:700;
    }

    /* Radio buttons */
    .stRadio label {
        color:white !important;
        font-weight:500;
    }

    /* FORCE LOGIN / REGISTER TEXT BRIGHT WHITE */
    div[role="radiogroup"] label {
    color:#ffffff !important;
    font-weight:700 !important;
    opacity:1 !important;
    }

    /* Text input fields */
    .stTextInput input {
        background-color:#1e293b;
        color:white;
        border:1px solid #38bdf8;
    }

    /* Password field */
    .stTextInput input::placeholder {
        color:#cbd5f5;
    }

    /* Buttons */
    .stButton button {
        background:#38bdf8;
        color:black;
        font-weight:700;
        border-radius:8px;
        border:none;
    }

    .stButton button:hover {
        background:#0ea5e9;
        color:white;
    }

    /* FORCE RADIO TEXT BRIGHT WHITE */
    div[role="radiogroup"] > label > div {
    color: #ffffff !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    }

    /* also ensure radio container text bright */
    div[role="radiogroup"] {
    color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)



    left, center, right = st.columns([3,2,3])

    with center:
        st.image("assets/logo.png", width=500)



    st.markdown(
        "<div class='title-text'>AI Nexus Studio</div>",
        unsafe_allow_html=True
    )


    st.write("")
    st.write("")


    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        menu = st.radio(
            "Choose",
            ["Login", "Register"],
            horizontal=True
        )


        if menu == "Login":

            st.subheader("Login")

            email = st.text_input("Email")

            password = st.text_input("Password", type="password")

            if st.button("Login", use_container_width=True):

                if login_user(email, password):

                    st.session_state["logged_in"] = True
                    st.session_state["email"] = email

                    st.success("Login Successful")
                    st.rerun()

                else:
                    st.error("Invalid login")

        else:

            st.subheader("Register")

            fullname = st.text_input("Full Name")

            email = st.text_input("Email Address")

            password = st.text_input("Password", type="password")

            if st.button("Register", use_container_width=True):

                success = register_user(fullname, email, password)

                if success:
                    st.success("Registration successful! Please login.")

                else:
                    st.error("Email already exists")