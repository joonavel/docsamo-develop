import streamlit as st
from utils import switch_page, show_sidebar, show_menu

print("settings session state:", st.session_state)
st.write("page2")

if st.button("게임으로 돌아가기"):
    switch_page(st.session_state.game_page)


show_menu(st.session_state.prev_page, "")
