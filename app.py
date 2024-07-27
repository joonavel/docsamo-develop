import streamlit as st

# 페이지 표시 및 타이틀
st.set_page_config(page_title="마춤뻡 마왕 vs. 맞춤법 용사", layout="wide")
st.title("마춤뻡 마왕 vs. 맞춤법 용사")

# 페이지 변수 초기화
if "service_started" not in st.session_state:
    st.session_state.index = False
    st.session_state.rounds = False


def start_service() -> None:
    """_summary_"""
    st.session_state.index = True
    st.session_state.service_started = True
    return


def enter_rounds() -> None:
    """_summary_"""
    # rounds 페이지의 유형은 5가지이다.
    # ["choice", "problem", "solve", "story", "ending"]
    st.session_state.index = False
    st.session_state.rounds = "choice"
    return


if st.button("SERVICE START!"):
    start_service()

if "service_started" in st.session_state:
    if st.session_state.index:
        st.write("index 페이지 입니다.")

        if st.button("ENTER ROUNDS"):
            enter_rounds()

    if st.session_state.rounds:
        round_type = st.session_state.rounds
        if round_type == "choice":
            st.write(f"{round_type} 페이지 입니다.")
        elif round_type == "story":
            st.write(f"{round_type} 페이지 입니다.")
        elif round_type == "problem":
            st.write(f"{round_type} 페이지 입니다.")
        elif round_type == "solve":
            st.write(f"{round_type} 페이지 입니다.")
        else:
            st.write(f"{round_type} 페이지 입니다.")
        print(st.session_state.index)
