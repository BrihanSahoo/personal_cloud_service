
import streamlit as st
import requests

from api import get_files, download_file, get_image


st.set_page_config(
    page_title="Dashboard",
    page_icon="📂",
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
📂 My Files
</h1>

<p class="subtitle">
Manage your personal cloud storage
</p>

</div>
""",
unsafe_allow_html=True
)



# Get files

response = get_files(token)



if response.status_code != 200:

    st.error(
        "Unable to load files"
    )

    st.stop()



files = response.json()



# Metrics

col1,col2,col3 = st.columns(3)



with col1:

    st.metric(
        "Total Files",
        len(files)
    )


with col2:

    images = [
        f for f in files
        if f["content_type"].startswith("image")
    ]

    st.metric(
        "Images",
        len(images)
    )


with col3:

    st.metric(
        "Storage",
        "Active"
    )



st.divider()



# Search

search = st.text_input(
    "🔍 Search files"
)



if search:


    files = [

        f for f in files

        if search.lower()
        in f["original_name"].lower()

    ]



if not files:


    st.info(
        "No files found"
    )

    st.stop()



# File grid


columns = st.columns(3)



for index,file in enumerate(files):


    with columns[index % 3]:


        st.markdown(
        """
        <div class="card">
        """,
        unsafe_allow_html=True
        )


        st.subheader(
            "📄 " + file["original_name"]
        )


        st.caption(
            file["content_type"]
        )



        # IMAGE PREVIEW

        if file["content_type"].startswith(
            "image"
        ):


            img = get_image(
                file["id"],
                token
            )


            if img.status_code == 200:


                st.image(
                    img.content,
                    use_container_width=True
                )



        # DOWNLOAD


        download = download_file(
            file["id"],
            token
        )


        if download.status_code == 200:


            st.download_button(

                label="⬇ Download",

                data=download.content,

                file_name=file["original_name"],

                mime=file["content_type"]

            )



        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )