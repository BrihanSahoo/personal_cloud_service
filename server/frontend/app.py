import streamlit as st

from api import login, signup


st.set_page_config(
    page_title="Personal Cloud",
    page_icon="☁️",
    layout="wide"
)


with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )



if "token" not in st.session_state:
    st.session_state.token=None


if "username" not in st.session_state:
    st.session_state.username=None



st.markdown(
"""
<div class="card">

<h1 class="title">
☁️ Personal Cloud
</h1>

<p class="subtitle">
Your private file storage server
</p>

</div>
""",
unsafe_allow_html=True
)



if st.session_state.token:

    st.success(
        f"Welcome {st.session_state.username}"
    )

    st.info(
        "Use the sidebar to manage your files"
    )

    st.stop()



login_tab, signup_tab = st.tabs(
    [
        "Login",
        "Create Account"
    ]
)



with login_tab:


    st.subheader("Login")


    email=st.text_input(
        "Email"
    )


    password=st.text_input(
        "Password",
        type="password"
    )


    if st.button("Login"):


        r=login(
            email,
            password
        )


        if r.status_code==200:


            data=r.json()

            st.session_state.token=data["access_token"]

            st.session_state.username=email

            st.rerun()


        else:

            st.error(
                "Invalid login"
            )



with signup_tab:


    st.subheader(
        "Create account"
    )


    username=st.text_input(
        "Username"
    )


    email=st.text_input(
        "Email",
        key="signup_email"
    )


    password=st.text_input(
        "Password",
        type="password",
        key="signup_password"
    )



    if st.button(
        "Sign Up"
    ):


        r=signup(
            username,
            email,
            password
        )


        if r.status_code==200:

            st.success(
                "Account created. Login now."
            )

        else:

            st.error(
                r.text
            )


if st.session_state.token:

    pages = {

        "Dashboard": "pages/Dashboard.py",

        "Upload": "pages/Upload.py",

        "Profile": "pages/Profile.py"

    }


    choice = st.sidebar.radio(
        "Navigation",
        pages.keys()
    )


    st.switch_page(
        pages[choice]
    )