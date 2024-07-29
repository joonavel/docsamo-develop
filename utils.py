import streamlit as st
import datetime
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def switch_page(page_name: str):
    """
    streamlit의 multipage간의 이동을
    사이드 바가 아닌 버튼 등으로 이용하기 위한 함수입니다.
    streamlit run으로 실행되는 main app의 이름은 page 변수에 저장 되며,
    main app을 교체할시 같이 바꾸어야 합니다.
    이동할 페이지 파일들은 main app과 같은 위치에 있는 pages 디렉토리에 존재해야 합니다.
    Args:
        page_name (str): 이동할 페이지 이름(.py 빼고)

    Raises:
        RerunException: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        """
        switch_page에서 입력받은 page_name을 정규화 하기 위한 함수입니다.
        _를 \\s 로 교체 후 소문자로 바꾸어 반환합니다.
        Args:
            name (str): switch_page 함수의 page_name argument

        Returns:
            str: 정규화된 page_name
        """
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("navigator.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config.get("page_name", "")) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [
        standardize_name(config.get("page_name", "")) for config in pages.values()
    ]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


def show_sidebar() -> None:
    """
    설정 및 분석 페이지로 이동하기 위해 사용되는
    사이드바를 불러옵니다.
    """
    with st.sidebar:
        if st.button("user"):
            switch_page("user")
        if st.button("user_analysis"):
            switch_page("user_analysis")
        if st.button("settings"):
            switch_page("settings")


def start_service() -> None:
    """
    stateful한 웹사이트를 위해 session_state에 저장할 변수를 초기화 하기위한 함수입니다.
    """
    if "service_started" not in st.session_state:
        st.session_state.service_started = True
        st.session_state.count = 0
        st.session_state.last_updated = datetime.time(0, 0)
        st.session_state.celsius = 50.0


def increment_counter(increment_value: int = 1) -> None:
    """
    statefulness를 확인하기 위한 예시 함수입니다.
    session_state의 count 값을 변화시킵니다.

    Args:
        increment_value (int): count에 더해질 값. Defaults to 1.
    """
    st.session_state.count += increment_value


def update_counter() -> None:
    """
    statefulness를 확인하기 위한 예시 함수입니다.
    session_state의 count, last_updated 값들을 변화시킵니다.
    """
    st.session_state.count += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time


def load_prompt(file_path: str) -> str:
    """
    prompt를 불러오는 함수입니다.

    Args:
        file_path (str): 파일 경로

    Returns:
        str : prompt
    """
    with open(file_path, "r", encoding="utf-8") as file:
        prompt = file.read().strip()
    return prompt


def generate_prompt(file_path: str, prompt_variable: str) -> ChatPromptTemplate:
    """
    prompt template를 만드는 함수

    Args:
        file_path (str): 파일 경로
        prompt_variable (str): prompt안에 변수

    Returns:
        ChatPromptTemplate: prompt template
    """
    system_prompt = load_prompt(file_path)
    custom_prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(system_prompt),
            HumanMessagePromptTemplate.from_template(prompt_variable),
        ]
    )
    return custom_prompt
