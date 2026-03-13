import streamlit as st
from auth.auth_db import register_user, login_user


def auth_page():

st.markdown("""
<style>

.title{
text-align:center;
font-size:60px;
font-weight:700;
color:#38bdf8;
margin-bottom:40px;
}

/* INPUT CONTAINER */
div[data-baseweb="input"]{
background:#1e293b !important;
border:2px solid #38bdf8 !important;
border-radius:10px !important;
padding:6px 10px !important;
}

/* INPUT FIELD */
div[data-baseweb="input"] input{
background:transparent !important;
border:none !important;
color:white !important;
font-size:16px !important;
}

/* REMOVE DEFAULT STREAMLIT INPUT BORDER */
div[data-baseweb="input"]:focus-within{
border:2px solid #0ea5e9 !important;
box-shadow:none !important;
}

/* REMOVE RED ERROR BORDER */
input:focus{
outline:none !important;
box-shadow:none !important;
}

/* BUTTON */
.stButton button{
height:48px;
width:100%;
font-size:17px;
border-radius:10px;
background:#38bdf8;
color:black;
font-weight:600;
border:none;
}

.stButton button:hover{
background:#0ea5e9;
color:white;
}

/* REMOVE FORM HINT TEXT COMPLETELY */
[data-testid="InputInstructions"]{
display:none !important;
}

</style>
""", unsafe_allow_html=True)


    col1, col2, col3 = st.columns([3,1,3])
    with col2:
        st.image("assets/logo.png", width=250)

    st.markdown("<div class='title'>AI Nexus Studio</div>", unsafe_allow_html=True)


    left, center, right = st.columns([4,2,4])

    with center:

        menu = st.radio("Choose", ["Login", "Register"], horizontal=True)


        if menu == "Login":

            st.subheader("Login")

            with st.form("login_form"):

                email = st.text_input(
                    "Email",
                    placeholder="Enter your email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Enter your password"
                )

                login_btn = st.form_submit_button("Login", use_container_width=True)

                if login_btn:

                    if login_user(email, password):

                        st.session_state.logged_in = True
                        st.session_state.email = email

                        st.success("Login Successful")
                        st.rerun()

                    else:
                        st.error("Invalid login")


        else:

            st.subheader("Register")

            with st.form("register_form"):

                fullname = st.text_input(
                    "Full Name",
                    placeholder="Enter your full name"
                )

                email = st.text_input(
                    "Email Address",
                    placeholder="Enter your email"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Create a password"
                )

                register_btn = st.form_submit_button("Register", use_container_width=True)

                if register_btn:

                    success = register_user(fullname, email, password)

                    if success:
                        st.success("Registration successful! Please login.")
                    else:
                        st.error("Email already exists")