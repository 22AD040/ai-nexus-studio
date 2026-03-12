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

/* TEXT INPUT WRAPPER */
div[data-testid="stTextInput"] > div{
display:flex !important;
align-items:center !important;
background:#1e293b !important;
border:2px solid #38bdf8 !important;
border-radius:10px !important;
height:48px !important;
padding-left:12px !important;
}

/* INPUT FIELD */
div[data-testid="stTextInput"] input{
background:transparent !important;
border:none !important;
color:white !important;
font-size:16px !important;
width:100% !important;
}

/* REMOVE STREAMLIT RED BORDER */
input:focus{
outline:none !important;
box-shadow:none !important;
}

/* PASSWORD EYE BUTTON */
div[data-testid="stTextInput"] button{
background:transparent !important;
border:none !important;
margin-right:10px !important;
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
}

.stButton button:hover{
background:#0ea5e9;
color:white;
}

</style>
""", unsafe_allow_html=True)


    # LOGO
    col1, col2, col3 = st.columns([3,1,3])
    with col2:
        st.image("assets/logo.png", width=180)


    st.markdown("<div class='title'>AI Nexus Studio</div>", unsafe_allow_html=True)


    # CENTER FORM
    left, center, right = st.columns([4,2,4])

    with center:

        menu = st.radio("Choose", ["Login", "Register"], horizontal=True)


        if menu == "Login":

            st.subheader("Login")

            email = st.text_input(
                "Email",
                placeholder="Enter your email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            if st.button("Login", use_container_width=True):

                if login_user(email, password):

                    st.session_state.logged_in = True
                    st.session_state.email = email

                    st.success("Login Successful")
                    st.rerun()

                else:
                    st.error("Invalid login")


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