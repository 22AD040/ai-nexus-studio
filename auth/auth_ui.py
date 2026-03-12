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
        margin-bottom:30px;
    }

    /* CARD STYLE */
    .card{
        padding:35px;
        border-radius:14px;
        background:rgba(15,23,42,0.6);
        backdrop-filter: blur(10px);
        border:1px solid rgba(56,189,248,0.2);
    }

    /* INPUT */
    div[data-testid="stTextInput"] input{
        height:46px !important;
        font-size:15px !important;
        border-radius:8px !important;
        background:#1e293b !important;
        color:white !important;
        border:1px solid #38bdf8 !important;
    }

    /* BUTTON */
    .stButton button{
        height:46px !important;
        font-size:16px !important;
        font-weight:600 !important;
        background:#38bdf8 !important;
        color:black !important;
        border-radius:8px !important;
        width:100%;
    }

    .stButton button:hover{
        background:#0ea5e9 !important;
        color:white !important;
    }

    h3{
        color:#38bdf8 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------- LOGO CENTER ----------
    c1, c2, c3 = st.columns([3,1,3])
    with c2:
        st.image("assets/logo.png", width=180)

    # ---------- TITLE ----------
    st.markdown(
        "<div class='title-text'>AI Nexus Studio</div>",
        unsafe_allow_html=True
    )

    # ---------- CENTER CARD ----------
    left, center, right = st.columns([1,2,1])

    with center:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        menu = st.radio(
            "Choose",
            ["Login", "Register"],
            horizontal=True
        )

        # ---------- LOGIN ----------
        if menu == "Login":

            st.subheader("Login")

            email = st.text_input("Email", placeholder="Enter your email")

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            if st.button("Login", use_container_width=True):

                if login_user(email, password):

                    st.session_state["logged_in"] = True
                    st.session_state["email"] = email

                    st.success("Login Successful")
                    st.rerun()

                else:
                    st.error("Invalid login")

        # ---------- REGISTER ----------
        else:

            st.subheader("Register")

            fullname = st.text_input("Full Name")

            email = st.text_input("Email Address")

            password = st.text_input(
                "Password",
                type="password"
            )

            if st.button("Register", use_container_width=True):

                success = register_user(fullname, email, password)

                if success:
                    st.success("Registration successful! Please login.")
                else:
                    st.error("Email already exists")

        st.markdown("</div>", unsafe_allow_html=True)