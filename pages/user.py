import streamlit as st
from utils import switch_page, show_sidebar

print("user session state:", st.session_state)
st.write("page2")

show_sidebar()