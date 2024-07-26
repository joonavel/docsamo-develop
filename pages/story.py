import streamlit as st
from utils import switch_page, show_sidebar

st.set_page_config("story page.")
print("story session state:", st.session_state)
st.write("story page")

if st.button("problem"):
    switch_page("problem")

show_sidebar()