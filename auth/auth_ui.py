import streamlit as st
from auth.auth_db import register_user, login_user


def auth_page():

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg,#020617,#0f172a,#020617);
        color:white;
    }

    /* TITLE */
    .title-text{
        text-align:center;
        font-size:60px;
        font-weight:650;
        color:#38bdf8;
        margin-top:-10px;
        margin-bottom:5px;
    }

    /* FORM CONTAINER */
    .login-card{
        max-width:520px;
        width:100%;
        margin:auto;
    }

    /* LABEL */
    label{
        color:white !important;
        font-size:15px !important;
        font-weight:600;
    }

    /* RADIO */
    .stRadio label{
        font-size:16px !important;
        font-weight:600 !important;
    }

    div[role="radiogroup"]{
        justify-content:center;
    }

    /* INPUT FIELD */
    .stTextInput input{
        height:45px !important;
        font-size:16px !important;
        border-radius:8px !important;
        background:#1e293b !important;
        color:white !important;
        border:1px solid #38bdf8 !important;
        width:100% !important;
    }

    div[data-testid="stTextInput"]{
        width:100% !important;
    }

    /* PLACEHOLDER */
    .stTextInput input::placeholder{
        color:#cbd5f5 !important;
    }

    /* BUTTON */
    .stButton button{
        height:45px !important;
        font-size:16px !important;
        font-weight:600 !important;
        background:#38bdf8 !important;
        color:black !important;
        border-radius:8px !important;
        width:100% !important;
    }

    .stButton button:hover{
        background:#0ea5e9 !important;
        color:white !important;
    }

    /* SUBHEADER */
    h3{
        color:#38bdf8 !important;
        font-size:22px;
    }

    </style>
    """, unsafe_allow_html=True)


    # ---------- LOGO ----------
    left, center, right = st.columns([1,2,1])

    with center:
        st.image("assets/logo.png", width=220)


    st.markdown(
        "<div class='title-text'>AI Nexus Studio</div>",
        unsafe_allow_html=True
    )


    st.write("")


    # ---------------- LOGIN FORM ----------------
    left, center, right = st.columns([1,3,1])

    with center:

        st.markdown("<div class='login-card'>", unsafe_allow_html=True)

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

        st.markdown("</div>", unsafe_allow_html=True)