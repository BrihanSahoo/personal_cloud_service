import streamlit as st

from api import get_files



st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)



# Check login

if "token" not in st.session_state or not st.session_state.token:

    st.warning(
        "Please login first"
    )

    st.stop()



token = st.session_state.token



# Header

st.markdown(
"""
<div class="card">

<h1 class="title">
👤 Profile
</h1>

<p class="subtitle">
Your account information
</p>

</div>
""",
unsafe_allow_html=True
)



# User info


username = st.session_state.get(
    "username",
    "User"
)



st.markdown(
f"""
<div class="card">

<h2>
👋 {username}
</h2>

<p>
Account Status:
<span style="color:green">
● Active
</span>
</p>

</div>
""",
unsafe_allow_html=True
)



# File statistics


response = get_files(token)



total_files = 0


if response.status_code == 200:

    total_files = len(
        response.json()
    )



col1,col2 = st.columns(2)



with col1:

    st.metric(
        "Total Files",
        total_files
    )


with col2:

    st.metric(
        "Storage",
        "Connected"
    )



st.divider()



# Account section


st.markdown(
"""
<div class="card">

<h3>
⚙️ Account
</h3>

<p>
Your files are stored on your personal Windows server.
</p>

<p>
Your authentication is protected using JWT tokens.
</p>

</div>
""",
unsafe_allow_html=True
)



# Logout


st.subheader(
""
)


if st.button(
    "🚪 Logout"
):

    st.session_state.token = None

    st.session_state.username = None

    st.success(
        "Logged out"
    )

    st.switch_page(
        "app.py"
    )