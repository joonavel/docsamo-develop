import streamlit as st
from utils import switch_page, show_sidebar, start_service


# session_state 값 초기화
start_service()
st.session_state.game_page = "navigator"

st.write("Here is Temporary Home")

if st.button("Choice"):
    switch_page("choice")

show_sidebar()
