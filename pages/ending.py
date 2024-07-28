import streamlit as st
from utils import switch_page, show_sidebar

st.set_page_config("ending page.")
print("ending session state:", st.session_state)
st.write("ending page")

st.session_state.game_page = "ending"

show_sidebar()
