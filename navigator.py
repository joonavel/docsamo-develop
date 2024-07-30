import streamlit as st
from utils import switch_page, start_service, show_menu


# session_state 값 초기화
start_service()
st.session_state.game_page = "navigator"

st.write("Here is Temporary Home")

if st.button("Choice"):
    switch_page("choice")

# show_sidebar()

# with st.sidebar.container():
#     st.write("2번 공간")

# with st.sidebar.container():
#     st.write("3번 공간")

show_menu(prev_page="", current_page=st.session_state.game_page)

# Section 2
st.sidebar.divider()
with st.sidebar.container(height=450):
    st.header("사용자 데이터 분석")
    st.write("분석 결과")
    st.image("https://via.placeholder.com/150", caption="강점")
    st.image("https://via.placeholder.com/150", caption="약점")

# Section 3
st.sidebar.divider()
with st.sidebar.container():
    st.header("사용자 정보")
    st.write("사용자: 닉네임")
    st.write("마지막 진행 상황")
