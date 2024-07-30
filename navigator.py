import streamlit as st
from utils import switch_page, start_service, show_menu, show_user_data


# session_state 값 초기화
start_service()
st.session_state.game_page = "navigator"

st.write("Here is Temporary Home")

if st.button("Choice"):
    switch_page("choice")


show_menu(prev_page="", current_page=st.session_state.game_page)

# Section 2
show_user_data(
    ["https://via.placeholder.com/150", "https://via.placeholder.com/150"], True, 450
)

# Section 3
st.sidebar.divider()
with st.sidebar.container():
    st.header("사용자 정보")
    st.write("사용자: 닉네임")
    st.write("마지막 진행 상황")
