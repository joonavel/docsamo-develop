import streamlit as st
from utils import switch_page, show_sidebar, show_menu

st.set_page_config("problem page.")
print("problem session state:", st.session_state)
st.write("page2")

st.session_state.game_page = "problem"

if st.button("solve"):
    switch_page("solve")

show_menu(st.session_state.prev_page, st.session_state.game_page)
