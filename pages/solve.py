import streamlit as st
from utils import switch_page, show_sidebar, show_menu

st.set_page_config("solve page.")
print("solve session state:", st.session_state)
st.write("solve page")

st.session_state.game_page = "solve"

if st.button("problem"):
    switch_page("problem")

if st.button("story"):
    switch_page("story")

show_menu(st.session_state.prev_page, st.session_state.game_page)
