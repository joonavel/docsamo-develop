import streamlit as st
from utils import switch_page, show_sidebar

st.set_page_config("solve page.")
print("solve session state:", st.session_state)
st.write("solve page")


if st.button("problem"):
    switch_page("problem")

if st.button("story"):
    switch_page("story")

show_sidebar()