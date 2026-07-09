import streamlit as st
import time

from api import upload_file



st.set_page_config(
    page_title="Upload",
    page_icon="⬆️",
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
⬆️ Upload Files
</h1>

<p class="subtitle">
Store your files securely on your personal server
</p>

</div>
""",
unsafe_allow_html=True
)



# Upload section

st.markdown(
"""
<div class="card">

<h3>
Choose files
</h3>

</div>
""",
unsafe_allow_html=True
)



files = st.file_uploader(

    "Drag and drop files here",

    accept_multiple_files=True

)



if files:


    st.write(
        f"Selected {len(files)} file(s)"
    )


    if st.button(
        "⬆ Upload Now"
    ):


        progress = st.progress(0)


        success = 0


        for index,file in enumerate(files):


            response = upload_file(
                file,
                token
            )


            if response.status_code == 200:

                success += 1


            progress.progress(
                int(
                    ((index+1)/len(files))*100
                )
            )


            time.sleep(0.2)



        if success == len(files):

            st.success(
                "All files uploaded successfully 🎉"
            )


        elif success > 0:

            st.warning(
                f"{success}/{len(files)} files uploaded"
            )


        else:

            st.error(
                "Upload failed"
            )



# Tips section


st.markdown(
"""
<div class="card">

<h3>
💡 Tips
</h3>

<ul>

<li>Images will show previews in Dashboard</li>

<li>Files are stored on your personal server</li>

<li>Keep your server laptop online for access</li>

</ul>

</div>
""",
unsafe_allow_html=True
)