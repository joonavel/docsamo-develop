import streamlit as st
from utils import (
    switch_page,
    start_service,
    show_menu,
    show_user_data,
    show_user_status,
)


# session_state 값 초기화
start_service()
st.session_state.game_page = "navigator"

st.write("Here is Temporary Home")

if st.button("Choice"):
    switch_page("choice")

# Section 1
show_menu(prev_page="", current_page=st.session_state.game_page, border=True)

# Section 2
show_user_data(
    ["https://via.placeholder.com/150", "https://via.placeholder.com/150"], True, 450
)

# Section 3
show_user_status("강호준", "solve", border=True)
