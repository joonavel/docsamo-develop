import streamlit as st
from utils import switch_page, show_sidebar, show_menu

st.set_page_config("ending page.")
print("ending session state:", st.session_state)
st.write("ending page")

st.session_state.game_page = "ending"

show_menu(st.session_state.prev_page, st.session_state.game_page)
