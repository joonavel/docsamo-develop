import streamlit as st
from utils import switch_page, show_sidebar

st.set_page_config("choice page.")
print("choice session state:", st.session_state)
st.write("choice page")

if st.button("story"):
    switch_page("story")

show_sidebar()
