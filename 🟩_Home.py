import streamlit as st
import time, toml, os

st.set_page_config(page_icon="🟩", page_title="AMH Dev Website | Home", initial_sidebar_state="collapsed")
hidden_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hidden_streamlit_style, unsafe_allow_html=True)

with open("../Configs/SiteRoot/info.toml", 'rb') as f:
    byte_string = f.read()

site_string = byte_string.decode('utf-8')  # Replace 'utf-8' with the appropriate character encoding
site_info = toml.loads(site_string)

site_root = site_info["server_info"]["domain"]
if len(site_root.split("/")) == 4:
    pass
else:
    site_root = f"{site_root}/"

tabs = st.tabs(["📌 Categories / Pages", "❇️ Website Information"])

with tabs[0]:
    st.title("🔵 Categories:", anchor="categories")

    try:
        pages_info = site_info["page_info"]["pages"]
        for page in pages_info:
            page_name = page['name']
            page_icon = page['icon']
            page_desc = page['desc']
            page_anchor = page['anchor']

            st.subheader(f"{page_icon} {page_name}", anchor=page_anchor)
            st.write(
                f"In \"[{page_name}]({site_root}{str(page_name).replace(' ', '_')})\" page," + " " + page_desc)
            st.divider()

    except Exception as e:
        st.error(icon="💥", body="Config file is on an invalid syntax / form.")
        st.info(e)

with tabs[1]:
    st.write("- **:green[This is my official site containing Programming & None-Programming Information].**")
    st.write("- **:red[This site contains Data Science & ML Packages as its engines]**.")
    st.write("- **:blue[This site is mostly coded in \"Python\" and some other things in \"C++\" & \"C#\"]**.")
